from django.db import models


class AbstractGraph(models.Model):
    """
    Creates "Abstract Graph Model"
    """

    class Meta:
        abstract = True


class AbstractEdge(models.Model):
    """
    Creates "Abstract Edge Model"
    """

    # ToDo: Need FK or M2M to graph based on config.
    #   Also, should there be a through-model for M2M?

    class Meta:
        abstract = True


class AbstractNode(models.Model):
    """
    Creates "Abstract Node Model"
    """

    # ToDo: Need FK or M2M to graph based on config.
    #   Also, should there be a through-model for M2M?

    class Meta:
        abstract = True


def cyclic_graph_factory(config):
    """
    Type: Subclassed Abstract Model
    Abstract methods of the Graph base model are implemented.
    """

    class CyclicGraph(AbstractGraph):
        class Meta:
            abstract = True

    return CyclicGraph()


def cyclic_edge_factory(config):
    """
    Type: Subclassed Abstract Model
    Abstract methods of the Edge base model are implemented.
    """

    class CyclicEdge(AbstractEdge):
        class Meta:
            abstract = True

    return CyclicEdge()


def cyclic_node_factory(config):
    """
    Type: Subclassed Abstract Model
    Abstract methods of the Node base model are implemented.
    """

    # edge_model_table = config.edge_model._meta.db_table

    class CyclicNode(AbstractNode):
        class Meta:
            abstract = True

    return CyclicNode()


def dag_graph_factory(config):
    """
    Type: Subclassed Abstract Model
    Abstract methods of the Graph base model are implemented.
    """

    class DAGGraph(AbstractGraph):
        class Meta:
            abstract = True

    return DAGGraph()


def dag_edge_factory(config):
    """
    Type: Subclassed Abstract Model
    Abstract methods of the Edge base model are implemented.
    """

    class DAGEdge(AbstractEdge):
        class Meta:
            abstract = True

    return DAGEdge()


def dag_node_factory(config):
    """
    Type: Subclassed Abstract Model
    Abstract methods of the Node base model are implemented.
    """

    # edge_model_table = config.edge_model._meta.db_table

    class DAGNode(AbstractNode):
        class Meta:
            abstract = True

    return DAGNode()


def polytree_graph_factory(config):
    """
    Type: Subclassed Abstract Model
    Abstract methods of the Graph base model are implemented.
    """

    class PolytreeGraph(AbstractGraph):
        class Meta:
            abstract = True

    return PolytreeGraph()


def polytree_edge_factory(config):
    """
    Type: Subclassed Abstract Model
    Abstract methods of the Edge base model are implemented.
    """

    class PolytreeEdge(AbstractEdge):
        class Meta:
            abstract = True

    return PolytreeEdge()


def polytree_node_factory(config):
    """
    Type: Subclassed Abstract Model
    Abstract methods of the Node base model are implemented.
    """

    # edge_model_table = config.edge_model._meta.db_table

    class PolytreeNode(AbstractNode):
        class Meta:
            abstract = True

    return PolytreeNode()


def arborescence_graph_factory(config):
    """
    Type: Subclassed Abstract Model
    Abstract methods of the Graph base model are implemented.
    """

    class ArborescenceGraph(AbstractGraph):
        class Meta:
            abstract = True

    return ArborescenceGraph()


def arborescence_edge_factory(config):
    """
    Type: Subclassed Abstract Model
    Abstract methods of the Edge base model are implemented.
    """

    class ArborescenceEdge(AbstractEdge):
        class Meta:
            abstract = True

    return ArborescenceEdge()


def arborescence_node_factory(config):
    """
    Type: Subclassed Abstract Model
    Abstract methods of the Node base model are implemented.
    """

    # edge_model_table = config.edge_model._meta.db_table

    class ArborescenceNode(AbstractNode):
        class Meta:
            abstract = True

    return ArborescenceNode()
