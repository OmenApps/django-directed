"""Functions for transforming RawQuerySet or other outputs of django-directed to alternate formats."""
import logging
from inspect import ismethod
from itertools import chain

from django.core.exceptions import FieldDoesNotExist
from django.db.models import Case
from django.db.models import When
from django.db.models.fields import DateTimeField
from django.db.models.fields import UUIDField
from django.db.models.fields.files import FileField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ManyToManyField

from django_directed.exceptions import GraphModelsCannotBeParsedError
from django_directed.exceptions import IncorrectInputTypeError
from django_directed.exceptions import IncorrectQuerySetTypeError


logger = logging.getLogger("django_directed")


def _ordered_filter(queryset, field_names, values):
    """Filters the provided queryset for 'field_name__in values' for each given field_name in [field_names].

    Orders results in the same order as provided values.
        For instance
            _ordered_filter(self.__class__.objects, "pk", pks)
        returns a queryset of the current class, with instances where the 'pk' field matches an pk in pks
    """
    if not isinstance(field_names, list):
        field_names = [field_names]
    case = []
    for pos, value in enumerate(values):
        when_condition = {field_names[0]: value, "then": pos}
        case.append(When(**when_condition))
    order_by = Case(*case)
    filter_condition = {field_name + "__in": values for field_name in field_names}
    return queryset.filter(**filter_condition).order_by(order_by)


def get_instance_characteristics(instance):
    """Returns a tuple of the node & edge model classes and the instance_type for the provided instance."""
    try:
        # Assume a queryset of nodes was provided
        _NodeModel = instance._meta.model  # noqa: N806
        _EdgeModel = instance._meta.model._meta.get_field("parents").through  # noqa: N806
        instance_type = "node"
    except FieldDoesNotExist:
        try:
            # Assume a queryset of edges was provided
            _EdgeModel = instance._meta.model  # noqa: N806
            _NodeModel = instance._meta.model._meta.get_field("parent").related_model  # noqa: N806
            instance_type = "edge"
        except FieldDoesNotExist as err:
            raise GraphModelsCannotBeParsedError from err
    return (_NodeModel, _EdgeModel, instance_type)


def get_queryset_characteristics(queryset):
    """Returns a tuple of the node & edge model classes and the queryset type for the provided queryset."""
    try:
        # Assume a queryset of nodes was provided
        _NodeModel = queryset.model  # noqa: N806
        _EdgeModel = queryset.model._meta.get_field("parents").through  # noqa: N806
        queryset_type = "nodes_queryset"
    except FieldDoesNotExist:
        try:
            # Assume a queryset of edges was provided
            _EdgeModel = queryset.model  # noqa: N806
            _NodeModel = queryset.model._meta.get_field("parent").related_model  # noqa: N806
            queryset_type = "edges_queryset"
        except FieldDoesNotExist as err:
            raise GraphModelsCannotBeParsedError from err
    return (_NodeModel, _EdgeModel, queryset_type)


def check_field_list(obj):
    """Verifies that obj is a list of strings.

    Used with model_to_dict to ensure that the field_list argument is valid.
    """
    return bool(obj) and all(isinstance(elem, str) for elem in obj)


def get_field_value(instance, field, date_strf=None):
    """Extracts the value of a field from a model instance.

    Used with model_to_dict to extract the value of a field from a model instance.
    """
    if isinstance(field, DateTimeField):
        dt = field.value_from_object(instance)
        return dt.strftime(date_strf) if date_strf else dt.timestamp()

    elif isinstance(field, ImageField):
        image = field.value_from_object(instance)
        return image.url if image else None

    elif isinstance(field, FileField):
        file = field.value_from_object(instance)
        return file.url if file else None

    elif isinstance(field, ManyToManyField):
        if instance.pk is None:
            return []
        else:
            qs = field.value_from_object(instance)
            if qs._result_cache is not None:
                return [item.pk for item in qs]
            else:
                # ToDo: Handle complex ManyToManyField cases
                return list(qs.values_list("pk", flat=True))

    elif isinstance(field, UUIDField):
        uuid = field.value_from_object(instance)
        return str(uuid) if uuid else None

    elif getattr(field, "editable", False):
        return field.value_from_object(instance)

    # ToDo: Process other types of model fields

    return None


def model_to_dict(instance, field_list, date_strf=None):
    """Returns a dictionary of {field_name: field_value} for a given model instance.

    e.g.: model_to_dict(myqueryset.first(), fields=["id",])
    For DateTimeFields, a formatting string can be provided
    Adapted from: https://ziwon.github.io/post/using_custom_model_to_dict_in_django/
    """
    if not check_field_list(field_list):
        raise IncorrectInputTypeError("field_list argument must be a list or tuple of fields")

    opts = instance._meta
    data = {}
    __fields = list(map(lambda a: a.split("__")[0], field_list or []))

    for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):
        if field_list and f.name not in __fields:
            continue

        value = get_field_value(instance, f, date_strf)
        if value is not None:
            data[f.name] = value

    # Handling additional functions or properties
    funcs = set(__fields) - set(list(data.keys()))
    for func in funcs:
        obj = getattr(instance, func)
        data[func] = obj() if ismethod(obj) else obj

    return data


def edges_from_nodes_queryset(nodes_queryset):
    """Given an Edge Model and a QuerySet or RawQuerySet of nodes, returns a queryset of the associated edges."""
    _NodeModel, _EdgeModel, queryset_type = get_queryset_characteristics(nodes_queryset)  # noqa: N806

    if queryset_type == "nodes_queryset":
        return _ordered_filter(_EdgeModel.objects, ["parent", "child"], nodes_queryset)
    raise IncorrectQuerySetTypeError("`queryset_type` must be 'nodes_queryset'")


def nodes_from_edges_queryset(edges_queryset):
    """Given a Node Model and a QuerySet or RawQuerySet of edges, returns a queryset of the associated nodes."""
    _NodeModel, _EdgeModel, queryset_type = get_queryset_characteristics(edges_queryset)  # noqa: N806

    if queryset_type == "edges_queryset":
        nodes_list = (
            _ordered_filter(
                _NodeModel.objects,
                [
                    f"{_NodeModel.__name__}_child",
                ],
                edges_queryset,
            )
            | _ordered_filter(
                _NodeModel.objects,
                [
                    f"{_NodeModel.__name__}_parent",
                ],
                edges_queryset,
            )
        ).values_list("pk")

        return _NodeModel.objects.filter(pk__in=nodes_list)
    raise IncorrectQuerySetTypeError
