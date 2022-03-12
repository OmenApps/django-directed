from dataclasses import dataclass, field
from typing import Union


@dataclass
class GraphConfig:
    """
    A GraphConfig object is used to configure details about the
      directed graph components.
    """

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

    # Models
    #   Model names should be `appname.ModelName`
    graph_fullname: str = ""
    edge_fullname: str = ""
    node_fullname: str = ""

    # Plugins
    #   A list or tuple of pluggy plugins to use with this graph
    graph_plugins: list = field(default_factory=list)
