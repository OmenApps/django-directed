# Edge

**WORK IN PROGRESS**

## Manager/QuerySet Methods

### Methods used for building/manipulating

- insert_node(edge, node, clone_to_rootside=False, clone_to_leafside=False, pre_save=None, post_save=None)

### Methods returning a queryset of Nodes

### Methods returning a queryset of Edges

### Methods returning a Boolean

### Methods returning other values

- from_node_queryset(nodes_queryset)
- descendants_edges(node, **kwargs)
- ancestors_edges(node, **kwargs)
- clan_edges(node, **kwargs)
- path_edges(start_node, end_node, **kwargs)

- path_is_valid(edges, **kwargs)

- sort(edges, **kwargs)


## Model Methods

### Methods used for building/manipulating an instance

- add_edge(from_node, to_node)
- insert_node(node, clone_to_rootside=False, clone_to_leafside=False, pre_save=None, post_save=None)

### Methods returning a queryset of Nodes

### Methods returning a queryset of Edges

### Methods returning a Boolean

### Methods returning other values