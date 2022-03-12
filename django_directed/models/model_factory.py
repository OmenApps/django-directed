from dataclasses import dataclass, field
from typing import Union

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
