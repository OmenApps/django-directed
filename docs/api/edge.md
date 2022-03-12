# Edge

**WORK IN PROGRESS**

## Manager/QuerySet Methods

None

### Methods used for building/manipulating

- insert_node(edge, node, clone_to_rootside=False, clone_to_leafside=False, pre_save=None, post_save=None)

### Methods returning a QuerySet of Nodes

None

### Methods returning a QuerySet of Edges

- descendants_edges(node, **kwargs)
- ancestors_edges(node, **kwargs)
- clan_edges(node, **kwargs)
- path_edges(start_node, end_node, **kwargs)

### Methods returning a Boolean

- path_is_valid(edges, **kwargs)

### Methods returning other values

- from_node_queryset(nodes_queryset)

- sort(edges, **kwargs)


## Model Methods

### Methods used for building/manipulating an instance



```{py:function} add_edge(from_node, to_node)

Provided with two Node instances, adds an edge between them.

:param Node node_from: The starting Node
:param Node node_to: The ending Node
:return: The newly created Edge
:rtype: Edge
```

- insert_node(node, clone_to_rootside=False, clone_to_leafside=False, pre_save=None, post_save=None)

### Methods returning a QuerySet of Nodes

None

### Methods returning a QuerySet of Edges

None

### Methods returning a Boolean

None

### Methods returning other values

None
