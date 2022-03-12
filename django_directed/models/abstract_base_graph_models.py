from operator import mod

from django.apps import apps
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.db import models
from django.db.models import Case, When
from django.utils.translation import gettext_lazy as _

from django_directed.context_managers import get_current_graph_instance
from django_directed.fields import CurrentGraphFKField
from django_directed.models.abstract_base_models import BaseEdge, BaseGraph, BaseNode
from django_directed.query_utils import _ordered_filter


def get_model_class(model_fullname: str) -> models.Model:
    """
    Provided with a model fullname (`app_name.ModelName`), Returns
        the associated model class
    """
    split_names = model_fullname.split(".")
    if not len(split_names) == 2:
        raise ImproperlyConfigured("Model fullnames in graph config must be specified as 'app_name.ModeName'")

    app_name, model_name = split_names

    try:
        model_class = apps.get_model(app_name, model_name)
    except (LookupError, ValueError) as e:
        raise ImproperlyConfigured(e)

    return model_class


def get_graph_aware_queryset(config):
    class GraphAwareQuerySet(models.QuerySet):
        def bulk_create(self, objs, batch_size=None, ignore_conflicts=False):
            objs = list(objs)
            for obj in objs:
                obj.provider = get_current_graph_instance()

            super().bulk_create(objs, batch_size, ignore_conflicts)

    return GraphAwareQuerySet


def get_graph_aware_manager(config):
    class GraphAwareManager(models.Manager):
        pass
        # def get_queryset(self):
        #     graph = get_current_graph_instance()
        #     queryset = super().get_queryset().filter(graph=graph)
        #     return queryset

    return GraphAwareManager


def base_graph(config):
    class AbstractGraph(BaseGraph):
        """
        Creates "Abstract Graph Model"
        """

        class Meta:
            abstract = True

        def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

        def clean_fields(self, exclude=None):
            super().clean_fields(exclude=exclude)

        def clean(self):
            super().clean()

    return AbstractGraph


def base_edge(config):
    class AbstractEdge(BaseEdge):
        """
        Creates "Abstract Edge Model"
        """

        graph_model_name = config.graph_fullname
        graph = CurrentGraphFKField(
            to=config.graph_fullname,
            null=True,
            related_name="graph_edges",
            related_query_name="graph_edges",
            # related_name="%(app_label)s_%(class)s_related",
            # related_query_name="%(app_label)s_%(class)ss",
        )

        node_model_name = config.node_fullname
        parent = models.ForeignKey(
            node_model_name,
            related_name="child_edges",
            on_delete=models.SET_NULL,
            null=True,
        )
        child = models.ForeignKey(
            node_model_name,
            related_name="parent_edges",
            on_delete=models.SET_NULL,
            null=True,
        )

        GraphAwareManager = get_graph_aware_manager(config)
        GraphAwareQuerySet = get_graph_aware_queryset(config)
        CombinedGraphManager = GraphAwareManager.from_queryset(GraphAwareQuerySet)
        objects = CombinedGraphManager()

        class Meta:
            abstract = True

        def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

        def clean_fields(self, exclude=None):
            super().clean_fields(exclude=exclude)

        def clean(self):
            super().clean()

    return AbstractEdge


def base_node(config):
    class AbstractNode(BaseNode):
        """
        Creates "Abstract Node Model"
        """

        graph_model_name = config.graph_fullname
        edge_model_name = config.edge_fullname
        # edge_model_table = edge_model._meta.db_table
        children_blank_null = config.children_blank_null

        GraphAwareManager = get_graph_aware_manager(config)
        GraphAwareQuerySet = get_graph_aware_queryset(config)
        CombinedGraphManager = GraphAwareManager.from_queryset(GraphAwareQuerySet)
        objects = CombinedGraphManager()

        children = models.ManyToManyField(
            "self",
            blank=children_blank_null,
            symmetrical=False,
            through=edge_model_name,
            through_fields=(  # ToDo: Verify this is in the correct order
                "parent",
                "child",
            ),
            related_name="parents",
        )

        @staticmethod
        def get_foreign_key_field(fk_instance=None):
            """
            Provided a model instance, checks if the edge model has a ForeignKey field to the
            model class of that instance, and then returns the associated field name, else None.
            """
            if fk_instance is not None:
                edge_model = get_model_class(config.edge_fullname)
                for field in edge_model._meta.get_fields():
                    if field.related_model is fk_instance._meta.model:
                        # Return the first field that matches
                        return field.name
            return None

        def get_pk_name(self):
            """Sometimes we set a field other than 'pk' for the primary key.
            This method is used to get the correct primary key field name for the
            model so that raw queries return the correct information."""
            return self._meta.pk.name

        def get_pk_type(self):
            """The pkid class may be set to a non-default type per-model or across the project.
            This method is used to return the postgres type name for the primary key field so
            that raw queries return the correct information."""
            django_pk_type = type(self._meta.pk).__name__

            if django_pk_type == "BigAutoField":
                return "bigint"
            elif django_pk_type == "UUIDField":
                return "uuid"
            else:
                return "integer"

        def ordered_queryset_from_pks(self, pks):
            """
            Generates a queryset, based on the current class and ordered by the provided pks
            """
            return _ordered_filter(self.__class__.objects, "pk", pks)

        @staticmethod
        def circular_checker(parent, child):
            if child in parent.self_and_ancestors():
                raise ValidationError("The object is an ancestor.")

        @staticmethod
        def duplicate_edge_checker(parent, child):
            if child in parent.self_and_descendants():
                raise ValidationError("The edge is a duplicate.")

        class Meta:
            abstract = True

        def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

        def clean_fields(self, exclude=None):
            super().clean_fields(exclude=exclude)

        def clean(self):
            super().clean()

    return AbstractNode
