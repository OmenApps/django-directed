"""Init file for models module."""
# from django_directed.models.abstract_base_graph_models import BaseEdge as _BaseEdge
# from django_directed.models.abstract_base_graph_models import BaseGraph as _BaseGraph
# from django_directed.models.abstract_base_graph_models import BaseNode as _BaseNode
from django_directed.models.model_factory import directed_factory


__all__ = [
    "directed_factory",
]
