# Graph

**WORK IN PROGRESS**

## Manager/QuerySet Methods

- clone()

### Methods used for building/manipulating

- add_node() add node to graph, optionally providing a list of parent nodes
- remove_nodes(nodes) removes nodes from the graph
- add_edge() adds connections or paths between nodes in graphs
- remove_edges(edges) removes connection or paths between nodes in graphs

### Methods returning a QuerySet of Nodes

None

### Methods returning a QuerySet of Edges

None

### Methods returning a Boolean

None

### Methods returning other values

```{py:function} node_count()

:return: Number of Nodes in the Graph
:rtype: int
```

```{py:function} edge_count()

:return: Number of Edges in the Graph
:rtype: int
```

```{py:function} graph_hash()

:return: Hash value for the Graph
:rtype: TBD
```


## Model Methods

### Methods used for building/manipulating an instance

None

### Methods returning a QuerySet of Nodes

None

### Methods returning a QuerySet of Edges

None

### Methods returning a Boolean

- contains_value() check if a graph instance contains a certain value



```{py:function} has_connection(node_from, node_to)

Provided with two Node instances, checks if a connection or path exists between them.

:param Node node_from: The starting Node
:param Node node_to: The ending Node
:return: True if path exists from `node_from` to `node_to`
:rtype: bool
```

### Methods returning other values

None
