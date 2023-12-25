from __future__ import annotations

from typing import TYPE_CHECKING

from django.core.exceptions import ValidationError
from django.db.models import Case
from django.db.models import When

from django_directed.models.abstract_base_graph_models import base_edge
from django_directed.models.abstract_base_graph_models import base_graph
from django_directed.models.abstract_base_graph_models import base_node


if TYPE_CHECKING:
    from django_directed.config import GraphConfig


def cyclic_graph_factory(config: GraphConfig):
    """Type: Subclassed Abstract Model. Abstract methods of the Graph base model are implemented."""

    class CyclicGraph(base_graph(config)):
        class Meta:
            abstract = True

    return CyclicGraph


def cyclic_edge_factory(config: GraphConfig):
    """Type: Subclassed Abstract Model. Abstract methods of the Edge base model are implemented."""

    class CyclicEdge(base_edge(config)):
        class Meta:
            abstract = True

        def save(self, *args, **kwargs):
            # Check for self links
            allow_self_links = config.allow_self_links
            if not allow_self_links:
                self.parent.__class__.self_link_check(self.parent, self.child)

            super().save(*args, **kwargs)

    return CyclicEdge


def cyclic_node_factory(config: GraphConfig):
    """Type: Subclassed Abstract Model. Abstract methods of the Node base model are implemented."""

    class CyclicNode(base_node(config)):
        class Meta:
            abstract = True

    return CyclicNode


def dag_graph_factory(config: GraphConfig):
    """Type: Subclassed Abstract Model. Abstract methods of the Graph base model are implemented."""

    class DAGGraph(base_graph(config)):
        class Meta:
            abstract = True

    return DAGGraph


def dag_edge_factory(config: GraphConfig):
    """Type: Subclassed Abstract Model. Abstract methods of the Edge base model are implemented."""

    class DAGEdge(base_edge(config)):
        class Meta:
            abstract = True

        def save(self, *args, **kwargs):
            # Check for circular links
            self.parent.__class__.circular_check(self.parent, self.child)

            super().save(*args, **kwargs)

    return DAGEdge


def dag_node_factory(config: GraphConfig):
    """Type: Subclassed Abstract Model. Abstract methods of the Node base model are implemented."""

    class DAGNode(base_node(config)):
        class Meta:
            abstract = True

    return DAGNode


def polytree_graph_factory(config: GraphConfig):
    """Type: Subclassed Abstract Model. Abstract methods of the Graph base model are implemented."""

    class PolytreeGraph(base_graph(config)):
        class Meta:
            abstract = True

    return PolytreeGraph


def polytree_edge_factory(config: GraphConfig):
    """Type: Subclassed Abstract Model. Abstract methods of the Edge base model are implemented."""

    class PolytreeEdge(base_edge(config)):
        class Meta:
            abstract = True

        def save(self, *args, **kwargs):
            # Check for circular links
            self.parent.__class__.circular_check(self.parent, self.child)

            super().save(*args, **kwargs)

    return PolytreeEdge


def polytree_node_factory(config: GraphConfig):
    """Type: Subclassed Abstract Model. Abstract methods of the Node base model are implemented."""

    class PolytreeNode(base_node(config)):
        class Meta:
            abstract = True

    return PolytreeNode


def arborescence_graph_factory(config: GraphConfig):
    """Type: Subclassed Abstract Model. Abstract methods of the Graph base model are implemented."""

    class ArborescenceGraph(base_graph(config)):
        class Meta:
            abstract = True

    return ArborescenceGraph


def arborescence_edge_factory(config: GraphConfig):
    """Type: Subclassed Abstract Model. Abstract methods of the Edge base model are implemented."""

    class ArborescenceEdge(base_edge(config)):
        class Meta:
            abstract = True

        def save(self, *args, **kwargs):
            # Check for circular links, if needed
            self.parent.__class__.circular_check(self.parent, self.child)

            super().save(*args, **kwargs)

    return ArborescenceEdge


def arborescence_node_factory(config: GraphConfig):
    """Type: Subclassed Abstract Model. Abstract methods of the Node base model are implemented."""

    class ArborescenceNode(base_node(config)):
        class Meta:
            abstract = True

    return ArborescenceNode
