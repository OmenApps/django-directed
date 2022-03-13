from dataclasses import dataclass
from enum import Enum

from django_directed.exceptions import ServiceDoesNotExistException
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

    def services_list(self):
        # Return list of registered services
        return list(self._builders.keys())

    def services_enum(self):
        # Return enum of registered services
        graph_type_names = [(name, name) for name in self.services_list()]
        return Enum(value="Graph Types", names=graph_type_names)

    def register(self, key, builder):
        # Registers model factory services
        self._builders[key] = builder

    def _create(self, config, **kwargs):
        key = config.graph_type.value
        builder = self._builders.get(key)
        if not builder:
            raise ServiceDoesNotExistException(f"Service '{key}' not found in list of services")
        return builder(config, **kwargs)

    def get(self, config: dataclass, **kwargs):
        # Creates and returns a new model factory for directed graph models
        return self._create(config, **kwargs)


# Register default factory services
factory = DirectedServiceFactory()
factory.register("CYCLIC", create_cyclic_service)
factory.register("DAG", create_dag_service)
factory.register("POLYTREE", create_polytree_service)
factory.register("ARBORESCENCE", create_arborescence_service)
