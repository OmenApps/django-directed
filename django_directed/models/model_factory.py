from dataclasses import dataclass, field

from django.apps import apps
from django.db import models

from django_directed.models.abstract_graph_models import (
    arborescence_edge_factory,
    arborescence_graph_factory,
    arborescence_node_factory,
    cyclic_edge_factory,
    cyclic_graph_factory,
    cyclic_node_factory,
    dag_edge_factory,
    dag_graph_factory,
    dag_node_factory,
    polytree_edge_factory,
    polytree_graph_factory,
    polytree_node_factory,
)


@dataclass
class GraphConfig:
    """
    A GraphConfig object is used to configure details about the
      directed graph components.
    """

    # Maximum number of children allowed for each node in the graph.
    #   A value of `-1` means any number of children are allowed.
    #   A value of `0` is ignored, and resolves to `-1`
    children_number_max: int = -1

    # Should null be allowed on the `children` field?
    children_blank_null: bool = True

    # Should multiple Edges be allowed between a pair of Nodes?
    allow_duplicate_edges: bool = False

    # Base model types
    graph_base_model: models.Model = models.Model
    edge_base_model: models.Model = models.Model
    node_base_model: models.Model = models.Model

    # Models
    #   Model names should be `appname.ModelName`
    graph_fullname: str = ""
    edge_fullname: str = ""
    node_fullname: str = ""

    # Plugins
    #   A list or tuple of plugins to use with this type of graph
    graph_plugins: list = field(default_factory=list)

    # def get_graph_model_class(self):
    #     return self.get_model_class(self.graph_fullname)

    # def get_edge_model_class(self):
    #     return self.get_model_class(self.edge_fullname)

    # def get_node_model_class(self):
    #     return self.get_model_class(self.node_fullname)


class CyclicService:
    """Returns the actual Graph, Edge, and Node models"""

    def __init__(self, config):
        self._instance = None
        self._config = config

    def graph(self):
        return cyclic_graph_factory(config=self._config)

    def edge(self):
        return cyclic_edge_factory(config=self._config)

    def node(self):
        return cyclic_node_factory(config=self._config)


def create_cyclic_service(config):
    return CyclicService(config)


class DAGService:
    """Returns the actual Graph, Edge, and Node models"""

    def __init__(self, config):
        self._instance = None
        self._config = config

    def graph(self):
        return dag_graph_factory(config=self._config)

    def edge(self):
        return dag_edge_factory(config=self._config)

    def node(self):
        return dag_node_factory(config=self._config)


def create_dag_service(config):
    return DAGService(config)


class PolytreeService:
    """Returns the actual Graph, Edge, and Node models"""

    def __init__(self, config):
        self._instance = None
        self._config = config

    def graph(self):
        return polytree_graph_factory(config=self._config)

    def edge(self):
        return polytree_edge_factory(config=self._config)

    def node(self):
        return polytree_node_factory(config=self._config)


def create_polytree_service(config):
    return PolytreeService(config)


class ArborescenceService:
    """Returns the actual Graph, Edge, and Node models"""

    def __init__(self, config):
        self._instance = None
        self._config = config

    def graph(self):
        return arborescence_graph_factory(config=self._config)

    def edge(self):
        return arborescence_edge_factory(config=self._config)

    def node(self):
        return arborescence_node_factory(config=self._config)


def create_arborescence_service(config):
    return ArborescenceService(config)


class DirectedServiceFactory:
    """Registers django-directed services"""

    def __init__(self):
        self._builders = {}

    def register(self, key, builder):
        self._builders[key] = builder

    def create(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)

    def get(self, service_id, **kwargs):
        return self.create(service_id, **kwargs)


# Register default factory services
factory = DirectedServiceFactory()
factory.register("CYCLIC", create_cyclic_service)
factory.register("DAG", create_dag_service)
factory.register("POLYTREE", create_polytree_service)
factory.register("ARBORESCENCE", create_arborescence_service)
