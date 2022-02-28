from dataclasses import dataclass

from django_directed.components import *


@dataclass
class GraphConfig:
    """
    A GraphConfig object is used to configure details about the directed graph components.
    """

    # Maximum number of children allowed for each node in the graph.
    #   A value of `-1` means any number of children are allowed.
    #   A value of `0` is ignored, and resolves to `-1`
    children_number_max: int = -1

    # If True and `children_number_max` is greater than 0, resulting graphs
    #   will be required to have exactly `children_number_max` children
    children_number_strict: bool = False

    # Should null be allowed on the `children` field?
    children_blank_null = True

    # Base model types
    graph_base_model = models.Model
    edge_base_model = models.Model
    node_base_model = models.Model

    # Models
    #   Model names should be `appname.ModelName` or `ModelName` if used within the same file
    graph_model_list = []
    edge_model_list = []
    node_model_name = ""


default_config = GraphConfig()


class CyclicService:
    # Returns the actual Graph, Edge, and Node models
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


class DirectedFactory:
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


# Register factory services
factory = DirectedFactory()
factory.register("CYCLIC", create_cyclic_service)
factory.register("DAG", create_dag_service)


def main():
    # Create Cyclic factory instance
    cyclic = factory.create("CYCLIC", config=default_config)

    # Create model instances
    MyCyclicGraph = cyclic.graph()
    MyCyclicEdge = cyclic.edge()
    MyCyclicNode = cyclic.node()

    # Create DAG factory instance
    dag = factory.create("DAG", config=default_config)

    # Create model instances
    MyDAGGraph = dag.graph()
    MyDAGEdge = dag.edge()
    MyDAGNode = dag.node()


if __name__ == "__main__":
    main()
