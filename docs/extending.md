# Extending Functionality in django-directed

You can extend django directed with new graph types, which can be used in a django package or directly within your project.

Start by creating new factory functions for the graph, edge, and node. The GraphConfig object is passed into each function, and can be used to customizing functionality of the returned model classes.

```python
from django.db import models

from django_directed.components import AbstractGraph, AbstractEdge, AbstractNode


def new_type_graph_factory(config):
    """
    Type: Subclassed Abstract Model
    Abstract methods of the Graph base model are implemented.
    """

    class NewTypeGraph(AbstractGraph):
        some_graph_field = models.IntegerField()

        class Meta:
            abstract = True

    return NewTypeGraph()


def new_type_edge_factory(config):
    """
    Type: Subclassed Abstract Model
    Abstract methods of the Edge base model are implemented.
    """

    class NewTypeEdge(AbstractEdge):
        some_edge_field = models.IntegerField()

        class Meta:
            abstract = True

    return NewTypeEdge()


def new_type_node_factory(config):
    """
    Type: Subclassed Abstract Model
    Abstract methods of the Node base model are implemented.
    """

    class NewTypeNode(AbstractNode):
        some_node_field = models.IntegerField()

        class Meta:
            abstract = True

    return NewTypeNode()
```

Create the service, with which the new graph types can be registered.

```python
class NewTypeService:
    # Returns the actual Graph, Edge, and Node models
    def __init__(self, config):
        self._instance = None
        self._config = config

    def graph(self):
        return new_type_graph_factory(config=self._config)

    def edge(self):
        return new_type_edge_factory(config=self._config)

    def node(self):
        return new_type_node_factory(config=self._config)


def create_new_type_service(config):
    return NewTypeService(config)
```

Register your new graph service.

```python
factory.register("NEW_TYPE", create_new_type_service)
```

As usual, within your app's `models.py`, instantiate the actual model instances.

```python
# Create NewType factory instance
new_type = factory.create("NEW_TYPE", config=my_custom_config)

# Create model instances
MyNewTypeGraph = new_type.graph()
MyNewTypeEdge = new_type.edge()
MyNewTypeNode = new_type.node()
```

