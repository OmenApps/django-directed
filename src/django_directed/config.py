import re
from typing import List
from typing import Type
from typing import Union

from django.db import models
from pydantic import BaseModel
from pydantic import validator

from django_directed.fields import CurrentGraphFKField
from django_directed.models import directed_factory


def validate_fullname(fullname: str) -> bool:
    r"""Validates model fullnames.

    <sphinx-skip>:
    Uses the following regex pattern:
        ^([a-z])                                                    Starts with 1 [a-z]
                ([a-zA-Z0-9_]+)                                     Match 1 or more [a-zA-Z0-9_]
                                (\.)                                Match 1 period
                                    ([a-zA-Z])                      Match 1 [a-zA-Z]
                                                ([a-zA-Z0-9_]+)$    Match 1 or more [a-zA-Z0-9_] at end
    <sphinx-skip>
    """
    pattern = re.compile(r"^([a-z])([a-zA-Z0-9_]+)(\.)([a-zA-Z])([a-zA-Z0-9_]+)$")
    if not bool(re.match(pattern, fullname)):
        raise ValueError("Model fullnames should be specified as `appame.ModelName`")
    return fullname


class GraphConfig(BaseModel):
    """
    A GraphConfig object is used to configure details about the
      directed graph components.
    """

    # Graph Type
    #   Default types include 'CYCLIC', 'DAG', 'POLYTREE', 'ARBORESCENCE'
    graph_type: directed_factory.services_enum()

    # Models
    #   Model names should be `appname.ModelName`
    graph_fullname: str
    edge_fullname: str
    node_fullname: str

    # Plugins
    #   A list or tuple of pluggy plugins to use with this graph
    # graph_plugins: list = field(default_factory=list)
    graph_plugins: list = []

    # Maximum number of children allowed for each node in the graph.
    #   A value of `None` means any number of children are allowed.
    #   Any value of less than 1 is ignored, and resolves to None
    children_quantity_max: Union[int, bool] = False

    # Should null be allowed on the `children` field?
    #   ToDo: Is this really needed?
    children_blank_null: bool = True

    # Should multiple Edges be allowed between a pair of Nodes?
    #   ToDo: Determine whether to fold this info the models themselves
    allow_duplicate_edges: bool = False

    # Should Nodes be allowed to link back to themselves?
    #   Only applies to CyclicEdge
    allow_self_links: bool = False

    # The `children` field in Node defaults to ManyToManyField,
    #   but can optionally use a subclass of ManyToManyField
    node_children_m2m_field: type[models.ManyToManyField] = models.ManyToManyField

    # The `graph` field in Edge defaults to CurrentGraphFKField,
    #   but can optionally use a subclass of CurrentGraphFKField
    edge_graph_fk_field: type[CurrentGraphFKField] = CurrentGraphFKField

    # The `parent`` and `child` fields in Edge default to ForeignKey,
    #   but can optionally use a subclass of ForeignKey
    edge_parent_fk_field: type[models.ForeignKey] = models.ForeignKey
    edge_child_fk_field: type[models.ForeignKey] = models.ForeignKey

    class Config:
        validate_assignment = True

    # Pydantic Validators

    @validator("edge_graph_fk_field", pre=True, always=True)
    def edge_graph_fk_field_correct_subclass(cls, value):
        if not issubclass(value, CurrentGraphFKField):
            raise ValueError("edge_graph_fk_field must be a subclass of CurrentGraphFKField")
        return value

    @validator("edge_parent_fk_field", "edge_child_fk_field", pre=True, always=True)
    def edge_parent_child_fk_fields_correct_subclass(cls, value):
        if not issubclass(value, models.ForeignKey):
            raise ValueError("edge_parent_fk_field and edge_child_fk_field must be a subclass of ForeignKey")
        return value

    @validator("node_children_m2m_field", pre=True, always=True)
    def node_children_m2m_field_is_m2m_subclass(cls, value):
        if not issubclass(value, models.ManyToManyField):
            raise ValueError("node_children_m2m_field must be a subclass of ManyToManyField")
        return value

    _validate_graph_fullname = validator("graph_fullname", allow_reuse=True)(validate_fullname)
    _validate_edge_fullname = validator("edge_fullname", allow_reuse=True)(validate_fullname)
    _validate_node_fullname = validator("node_fullname", allow_reuse=True)(validate_fullname)
