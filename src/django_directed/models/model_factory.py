from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING

from django_directed.exceptions import ServiceDoesNotExistException
from django_directed.models.abstract_graph_models import arborescence_edge_factory
from django_directed.models.abstract_graph_models import arborescence_graph_factory
from django_directed.models.abstract_graph_models import arborescence_node_factory
from django_directed.models.abstract_graph_models import cyclic_edge_factory
from django_directed.models.abstract_graph_models import cyclic_graph_factory
from django_directed.models.abstract_graph_models import cyclic_node_factory
from django_directed.models.abstract_graph_models import dag_edge_factory
from django_directed.models.abstract_graph_models import dag_graph_factory
from django_directed.models.abstract_graph_models import dag_node_factory
from django_directed.models.abstract_graph_models import polytree_edge_factory
from django_directed.models.abstract_graph_models import polytree_graph_factory
from django_directed.models.abstract_graph_models import polytree_node_factory


if TYPE_CHECKING:
    from django_directed.config import GraphConfig


class CyclicService:
    """Returns the actual Graph, Edge, and Node models"""

    def __init__(self, config: GraphConfig):
        self._instance = None
        self._config = config

    def graph(self):
        return cyclic_graph_factory(config=self._config)

    def edge(self):
        return cyclic_edge_factory(config=self._config)

    def node(self):
        return cyclic_node_factory(config=self._config)


def create_cyclic_service(config: GraphConfig):
    return CyclicService(config)


class DAGService:
    """Returns the actual Graph, Edge, and Node models"""

    def __init__(self, config: GraphConfig):
        self._instance = None
        self._config = config

    def graph(self):
        return dag_graph_factory(config=self._config)

    def edge(self):
        return dag_edge_factory(config=self._config)

    def node(self):
        return dag_node_factory(config=self._config)


def create_dag_service(config: GraphConfig):
    return DAGService(config)


class PolytreeService:
    """Returns the actual Graph, Edge, and Node models"""

    def __init__(self, config: GraphConfig):
        self._instance = None
        self._config = config

    def graph(self):
        return polytree_graph_factory(config=self._config)

    def edge(self):
        return polytree_edge_factory(config=self._config)

    def node(self):
        return polytree_node_factory(config=self._config)


def create_polytree_service(config: GraphConfig):
    return PolytreeService(config)


class ArborescenceService:
    """Returns the actual Graph, Edge, and Node models"""

    def __init__(self, config: GraphConfig):
        self._instance = None
        self._config = config

    def graph(self):
        return arborescence_graph_factory(config=self._config)

    def edge(self):
        return arborescence_edge_factory(config=self._config)

    def node(self):
        return arborescence_node_factory(config=self._config)


def create_arborescence_service(config: GraphConfig):
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

    def _create(self, config: GraphConfig, **kwargs):
        key = config.graph_type.value
        builder = self._builders.get(key)
        if not builder:
            raise ServiceDoesNotExistException(f"Service '{key}' not found in list of services")
        return builder(config, **kwargs)

    def get(self, config: GraphConfig, **kwargs):
        # Creates and returns a new model factory for directed graph models
        return self._create(config, **kwargs)


# Register default factory services
directed_factory = DirectedServiceFactory()
directed_factory.register("CYCLIC", create_cyclic_service)
directed_factory.register("DAG", create_dag_service)
directed_factory.register("POLYTREE", create_polytree_service)
directed_factory.register("ARBORESCENCE", create_arborescence_service)
