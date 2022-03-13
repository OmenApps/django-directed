import re
from typing import List, Union

from pydantic import BaseModel, validator

from django_directed.models.model_factory import factory


def validate_fullname(fullname: str) -> bool:
    """
    Validates model fullnames using the following regex pattern:
        ^([a-z])                                                Starts with 1 [a-z]
                ([a-zA-Z0-9_]+)                                 Match 1 or more [a-zA-Z0-9_]
                            (\.)                                Match 1 period
                                ([a-zA-Z])                      Match 1 [a-zA-Z]
                                            ([a-zA-Z0-9_]+)$    Match 1 or more [a-zA-Z0-9_] at end
    """
    pattern = re.compile("^([a-z])([a-zA-Z0-9_]+)(\.)([a-zA-Z])([a-zA-Z0-9_]+)$")
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
    graph_type: factory.services_enum()

    # Models
    #   Model names should be `appname.ModelName`
    graph_fullname: str
    edge_fullname: str
    node_fullname: str

    # Plugins
    #   A list or tuple of pluggy plugins to use with this graph
    # graph_plugins: list = field(default_factory=list)
    graph_plugins: List = []

    # Maximum number of children allowed for each node in the graph.
    #   A value of `None` means any number of children are allowed.
    #   Any value of less than 1 is ignored, and resolves to None
    children_number_max: Union[int, None] = None

    # Should null be allowed on the `children` field?
    #   ToDo: Is this really needed?
    children_blank_null: bool = True

    # Should multiple Edges be allowed between a pair of Nodes?
    #   ToDo: Determine whether to fold this info the models themselves
    allow_duplicate_edges: bool = False

    _validate_graph_fullname = validator("graph_fullname", allow_reuse=True)(validate_fullname)
    _validate_edge_fullname = validator("edge_fullname", allow_reuse=True)(validate_fullname)
    _validate_node_fullname = validator("node_fullname", allow_reuse=True)(validate_fullname)
