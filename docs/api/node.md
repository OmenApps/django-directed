# Node

**WORK IN PROGRESS**

## Manager/QuerySet Methods

### Methods used for building/manipulating

### Methods returning a queryset of Nodes
- roots(node=None)
- leaves(node=None)

### Methods returning a queryset of Edges

### Methods returning a Boolean

### Methods returning other values



## Model Methods

### Methods used for building/manipulating an instance

```{py:function} add_child(child, **kwargs)

Provided with a Node instance, attaches that instance as a child to the current Node instance

:param Node child: The Node to be added as a child
:return: The newly created Edge between self and child
:rtype: Edge
```

```{py:function} add_children(children, **kwargs)

Provided with a QuerySet of Node instances, attaches those instances as children of the current Node instance

:param QuerySet children: The Nodes to be added as children
:return: The newly created Edges between self and children
:rtype: list
```

- remove_child(child, delete_node=False)
- remove_children(children, delete_node=False)
- remove_all_children(delete_node=False)
- 
- add_parent(parent, *args, **kwargs)
- add_parents(parent, *args, **kwargs)
- remove_parent(parent, delete_node=False)
- remove_parents(parents, delete_node=False)
- remove_all_parents(delete_node=False)

### Methods returning a queryset of Nodes
- ancestors(**kwargs)
- self_and_ancestors(**kwargs)
- ancestors_and_self(**kwargs)
- descendants(**kwargs)
- descendants_count(self)
- self_and_descendants(**kwargs)
- descendants_and_self(**kwargs)
- clan(**kwargs)
- siblings(self)
- siblings_and_self(self)
- partners(self)
- partners_count(self)
- partners_and_self(self)
- path(ending_node, **kwargs)
- paths(ending_node, **kwargs)
- connected_graph(**kwargs)
- roots(self)
- leaves(self)

- * Others to consider:
- immediate_family (parents, self and childred)
- piblings (aka: aunts/uncles)
- niblings (aka: nieces/nephews)
- cousins

### Methods returning a queryset of Edges
- descendants_edges(self)
- ancestors_edges(self)
- clan_edges(self)

### Methods returning a Boolean
- path_exists_from(starting_node, **kwargs)
- path_exists_to(ending_node, **kwargs)
- is_root(self)
- is_leaf(self)
- is_island(self)
- is_ancestor_of(ending_node, **kwargs)
- is_descendant_of(ending_node, **kwargs)
- is_sibling_of(ending_node)
- is_partner_of(ending_node)

### Methods returning other valuesancestors_count(self)
- clan_count(self)
- siblings_count(self)
- distance(ending_node, **kwargs)
- node_depth(self)
- connected_graph_node_count(**kwargs)
- descendants_tree(self)
- ancestors_tree(self)


