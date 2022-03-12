# Node

**WORK IN PROGRESS**

## Manager/QuerySet Methods

### Methods used for building/manipulating

### Methods returning a queryset of Nodes

```{py:function} roots(node=None)

Returns a QuerySet of all root nodes (nodes with no parents) in the Node model. If a node instance is specified, returns only the roots for that node.

:param Node node: (optional)
:return: None
:rtype: QuerySet
```

```{py:function} leaves(node=None)

Returns a QuerySet of all leaf nodes (nodes with no children) in the Node model. If a node instance is specified, returns only the leaves for that node.

:param Node node: (optional)
:return: None
:rtype: QuerySet
```

### Methods returning a queryset of Edges

### Methods returning a Boolean

### Methods returning other values



## Model Methods

### Methods used for building/manipulating an instance

```{py:function} add_child(child, **kwargs)

Provided with a Node instance, attaches that instance as a child to the current Node instance.

:param Node child: The Node to be added as a child
:return: The newly created Edge between self and child
:rtype: Edge
```

```{py:function} add_children(children, **kwargs)

Provided with a QuerySet of Node instances, attaches those instances as children of the current Node instance.

:param QuerySet children: The Nodes to be added as children
:return: The newly created Edges between self and children
:rtype: list
```

```{py:function} add_parent(parent, **kwargs)

Provided with a Node instance, attaches that instance as a parent to the current Node instance.

:param Node parent: The Node to be added as a parent
:return: The newly created Edge between self and parent
:rtype: Edge
```

```{py:function} add_parents(parents, **kwargs)

Provided with a QuerySet of Node instances, attaches those instances as parents of the current Node instance.

:param QuerySet parents: The Nodes to be added as parents
:return: The newly created Edges between self and parents
:rtype: list
```

```{py:function} remove_child(child, delete_node=False)

Removes the edge connecting this node to child if a child Node instance is provided. Optionally deletes the child node as well.

:param Node child: The Node to be removed as a child
:return: None
:rtype: None
```

```{py:function} remove_children(children, **kwargs)

Provided with a QuerySet of Node instances, removes those instances as children of the current Node instance.

:param QuerySet children: The Nodes to be removed as children
:return: None
:rtype: None
```

```{py:function} remove_all_children(delete_node=False)

Removes all children of the current Node instance, optionally deleting self as well.

:param QuerySet children: The Nodes to be removed as children
:return: None
:rtype: None
```

```{py:function} remove_parent(parent, delete_node=False)

Removes the edge connecting this node to parent if a parent Node instance is provided. Optionally deletes the parent node as well.

:param Node parent: The Node to be removed as a parent
:return: None
:rtype: None
```

```{py:function} remove_parents(parents, **kwargs)

Provided with a QuerySet of Node instances, removes those instances as parents of the current Node instance.

:param QuerySet parents: The Nodes to be removed as parents
:return: None
:rtype: None
```

```{py:function} remove_all_parents(delete_node=False)

Removes all parents of the current Node instance, optionally deleting self as well.

:param QuerySet parents: The Nodes to be removed as parents
:return: None
:rtype: None
```

### Methods returning a queryset of Nodes

- ancestors(**kwargs)
- self_and_ancestors(**kwargs)
- ancestors_and_self(**kwargs)
- descendants(**kwargs)
- descendants_count()
- self_and_descendants(**kwargs)
- descendants_and_self(**kwargs)
- clan(**kwargs)
- siblings()
- siblings_and_self()
- partners()
- partners_count()
- partners_and_self()
- path(ending_node, **kwargs)
- paths(ending_node, **kwargs)
- connected_graph(**kwargs)


```{py:function} roots(node=None)

Returns a QuerySet of all root nodes, if any, for the current Node.

:param Node node: (optional)
:return: None
:rtype: QuerySet
```

```{py:function} leaves(node=None)

Returns a QuerySet of all leaf nodes, if any, for the current Node.

:param Node node: (optional)
:return: None
:rtype: QuerySet
```


- *Others to consider:*
- immediate_family (parents, self and childred)
- piblings (aka: aunts/uncles)
- niblings (aka: nieces/nephews)
- cousins

### Methods returning a queryset of Edges

- descendants_edges()
- ancestors_edges()
- clan_edges()

### Methods returning a Boolean

- path_exists_from(starting_node, **kwargs)
- path_exists_to(ending_node, **kwargs)
- is_root()
- is_leaf()
- is_island()
- is_ancestor_of(ending_node, **kwargs)
- is_descendant_of(ending_node, **kwargs)
- is_sibling_of(ending_node)
- is_partner_of(ending_node)

### Methods returning other values

- ancestors_count()
- clan_count()
- siblings_count()
- distance(ending_node, **kwargs)
- node_depth()
- connected_graph_node_count(**kwargs)
- descendants_tree()
- ancestors_tree()


