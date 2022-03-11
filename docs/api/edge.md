# Edge

**WORK IN PROGRESS**

## Manager/QuerySet Methods

### Methods used for building/manipulating
- insert_node(self, edge, node, clone_to_rootside=False, clone_to_leafside=False, pre_save=None, post_save=None)

### Methods returning a queryset of Nodes

### Methods returning a queryset of Edges

### Methods returning a Boolean

### Methods returning other values
- from_node_queryset(self, nodes_queryset)
- descendants_edges(self, node, **kwargs)
- ancestors_edges(self, node, **kwargs)
- clan_edges(self, node, **kwargs)
- path_edges(self, start_node, end_node, **kwargs)

- path_is_valid(self, edges, **kwargs)

- sort(self, edges, **kwargs)


## Model Methods

### Methods used for building/manipulating an instance
- add_edge(self, from_node, to_node)
- insert_node(self, node, clone_to_rootside=False, clone_to_leafside=False, pre_save=None, post_save=None)

### Methods returning a queryset of Nodes

### Methods returning a queryset of Edges

### Methods returning a Boolean

### Methods returning other values