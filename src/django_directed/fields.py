"""Custom model fields for Django Directed.""" ""
import logging

from django.db import models
from django.utils.translation import gettext_lazy as _

from django_directed.context_managers import get_current_graph_instance


logger = logging.getLogger("django_directed")


class CurrentGraphFKField(models.ForeignKey):
    """A ForeignKey field that defaults to the current Graph instance."""

    # ToDo: Need to add formfield() method

    description = _("Foreign Key with default to associated Graph model instance")

    def __init__(self, *args, **kwargs):  # noqa: D107
        self.on_update = kwargs.pop("on_update", False)
        self.graph_fullname = kwargs.pop("graph_fullname", None)

        if "on_delete" not in kwargs:
            kwargs["on_delete"] = models.CASCADE

        if self.on_update:
            kwargs["editable"] = False
            kwargs["blank"] = True

        super().__init__(**kwargs)

    def pre_save(self, model_instance, add):
        """Sets the value of the field on save."""
        if self.on_update:
            value = get_current_graph_instance(self.graph_fullname)
            if value is not None:
                value = value.pk
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)

    def deconstruct(self):
        """Deconstructs the field."""
        name, path, args, kwargs = super().deconstruct()
        if self.on_update:
            kwargs["on_update"] = self.on_update
            del kwargs["blank"]
            del kwargs["editable"]

        return name, path, args, kwargs
