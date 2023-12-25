# Extending Functionality

Beyond making modifications directly within your project (e.g. inheriting and extending the provided models & managers), there are two ways of extending django-directed for use in additional projects or for community use.

## Custom model factories

You can create new django-directed graph types with your own graph factories, which can be used directly within your project or in an installable django package for reuse.

### Create a new factory

Start by creating new factory functions for the graph, edge, and node. Like any other graph in django-directed, the GraphConfig object is passed into each function, and is used for customizing functionality of the returned model classes.

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

### Create the service

The service makes it possible to register the new factory within django-directed.

```python
class NewTypeService:
    """Returns the actual Graph, Edge, and Node models"""
    
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

### Register your new graph service

Now that the factory and service for our new graph type has been built, we can register the service in our django project and make use of the resulting models.

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

## Pluggy Plugins

Throughout django-directed, [pluggy](https://pluggy.readthedocs.io/en/stable/) hooks have been added to 

## Combined approach