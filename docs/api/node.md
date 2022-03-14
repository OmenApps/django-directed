# Node

## Manager/QuerySet Methods

### Methods used for building/manipulating

None

### Methods returning a QuerySet of Nodes

```{py:function} roots(node=None)

Returns a QuerySet of all root Nodes (nodes with no parents) in the Node model.

:param Node node: (optional) if specified, returns only the roots for that node
:return: Root Nodes
:rtype: QuerySet
```

```{py:function} leaves(node=None)

Returns a QuerySet of all leaf Nodes (nodes with no children) in the Node model.

:param Node node: (optional) if specified, returns only the leaves for that node
:return: Leaf Nodes
:rtype: QuerySet
```

```{py:function} islands()

Returns a QuerySet of all Nodes with no parents or children (degree 0).

:return: Island Nodes
:rtype: QuerySet
```

### Methods returning a QuerySet of Edges

None

### Methods returning a Boolean

None

### Methods returning other values

None



## Model Methods

### Methods used for building/manipulating an instance

```{py:function} add_child(child)

Provided with a Node instance, attaches that instance as a child to the current Node instance.

:param Node child: The Node to be added as a child
:return: The newly created Edge between self and child
:rtype: Edge
```

```{py:function} add_children(children)

Provided with a QuerySet of Node instances, attaches those instances as children of the current Node instance.

:param QuerySet children: The Nodes to be added as children
:return: The newly created Edges between self and children
:rtype: list
```

```{py:function} add_parent(parent)

Provided with a Node instance, attaches that instance as a parent to the current Node instance.

:param Node parent: The Node to be added as a parent
:return: The newly created Edge between self and parent
:rtype: Edge
```

```{py:function} add_parents(parents)

Provided with a QuerySet of Node instances, attaches those instances as parents of the current Node instance.

:param QuerySet parents: The Nodes to be added as parents
:return: The newly created Edges between self and parents
:rtype: list
```

```{py:function} remove_child(child, delete_node=False)

Removes the edge connecting this node to child if a child Node instance is provided. Optionally deletes the child node as well.

:param Node child: The Node to be removed as a child
:return: True if any Nodes were removed, otherwise False
:rtype: bool
```

```{py:function} remove_children(children)

Provided with a QuerySet of Node instances, removes those instances as children of the current Node instance.

:param QuerySet children: The Nodes to be removed as children
:return: True if any Nodes were removed, otherwise False
:rtype: bool
```

```{py:function} remove_all_children(delete_node=False)

Removes all children of the current Node instance, optionally deleting self as well.

:param QuerySet children: The Nodes to be removed as children
:return: True if any Nodes were removed, otherwise False
:rtype: bool
```

```{py:function} remove_parent(parent, delete_node=False)

Removes the edge connecting this node to parent if a parent Node instance is provided. Optionally deletes the parent node as well.

:param Node parent: The Node to be removed as a parent
:return: True if any Nodes were removed, otherwise False
:rtype: bool
```

```{py:function} remove_parents(parents)

Provided with a QuerySet of Node instances, removes those instances as parents of the current Node instance.

:param QuerySet parents: The Nodes to be removed as parents
:return: True if any Nodes were removed, otherwise False
:rtype: bool
```

```{py:function} remove_all_parents(delete_node=False)

Removes all parents of the current Node instance, optionally deleting self as well.

:param QuerySet parents: The Nodes to be removed as parents
:return: True if any Nodes were removed, otherwise False
:rtype: bool
```

### Methods returning a QuerySet of Nodes


```{py:function} ancestors()

Returns all Nodes in connected paths in a rootward direction.

:return: Nodes
:rtype: QuerySet
```


```{py:function} self_and_ancestors()

Returns all Nodes in connected paths in a rootward direction, prepending self.

:return: Nodes
:rtype: QuerySet
```


```{py:function} ancestors_and_self()

Returns all Nodes in connected paths in a rootward direction, appending self.

:return: Nodes
:rtype: QuerySet
```

```{py:function} descendants()

Returns all Nodes in connected paths in a leafward direction.

:return: Nodes
:rtype: QuerySet
```


```{py:function} self_and_descendants()

Returns all Nodes in connected paths in a leafward direction, prepending self.

:return: Nodes
:rtype: QuerySet
```


```{py:function} descendants_and_self()

Returns all Nodes in connected paths in a leafward direction, appending self.

:return: Nodes
:rtype: QuerySet
```

```{py:function} siblings()

Returns all Nodes that share a parent with this Node.

:return: Nodes
:rtype: QuerySet
```


```{py:function} self_and_siblings()

Returns all Nodes that share a parent with this Node, prepending self.

:return: Nodes
:rtype: QuerySet
```


```{py:function} siblings_and_self()

Returns all Nodes that share a parent with this Node, appending self.

:return: Nodes
:rtype: QuerySet
```

```{py:function} partners()

Returns all Nodes that share a child with this Node.

:return: Nodes
:rtype: QuerySet
```


```{py:function} self_and_partners()

Returns all Nodes that share a child with this Node, prepending self.

:return: Nodes
:rtype: QuerySet
```


```{py:function} partners_and_self()

Returns all Nodes that share a child with this Node, appending self.

:return: Nodes
:rtype: QuerySet
```


```{py:function} clan()

Returns a QuerySet with all ancestor Nodes, self, and all descendant Nodes.

:return: Nodes
:rtype: QuerySet
```


```{py:function} connected_graph()

Returns all nodes connected in any way to the current Node instance.

:param Node directional: (optional) if True, path searching operates normally (in leafward direction), if False search operates in both directions
:return: Nodes
:rtype: QuerySet
```


```{py:function} shortest_path(target_node)

Returns the shortest path from self to target Node. Resulting Queryset is sorted leafward, regardless of the relative position of starting and ending nodes.

:param Node target_node: The target Node for searching
:param Node directional: (optional) if True, path searching operates normally (in leafward direction), if False search operates in both directions
:return: Nodes
:rtype: QuerySet
```


```{py:function} all_paths(target_node)

Returns all paths from self to target Node. Resulting Queryset is sorted leafward, regardless of the relative position of starting and ending nodes.

:param Node target_node: The target Node for searching
:param Node directional: (optional) if True, path searching operates normally (in leafward direction), if False search operates in both directions
:return: Nodes
:rtype: QuerySet
```


```{py:function} roots()

Returns a QuerySet of all root Nodes, if any, for the current Node.

:return: Root Nodes
:rtype: QuerySet
```

```{py:function} leaves()

Returns a QuerySet of all leaf Nodes, if any, for the current Node.

:return: Leaf Nodes
:rtype: QuerySet
```


For future consideration:

- immediate_family (parents, self and children)
- piblings (aka: aunts/uncles)
- niblings (aka: nieces/nephews)
- cousins

### Methods returning a QuerySet of Edges


```{py:function} ancestor_edges()

Ancestor Edge instances for the current Node.

:return: Ancestor Edges
:rtype: QuerySet
```


```{py:function} descendant_edges()

Descendant Edge instances for the current Node.

:return: Descendant Edges
:rtype: QuerySet
```


```{py:function} clan_edges()

Clan Edge instances for the current Node.

:return: Clan Edges
:rtype: QuerySet
```


### Methods returning a Boolean

```{py:function} is_root()

Returns True if the current Node instance has no parents (Node has an in-degree 0 and out-degree >= 0).

:rtype: bool
```


```{py:function} is_leaf()

Returns True if the current Node instance has no children (Node has an in-degree >=0 and out-degree 0).

:rtype: bool
```


```{py:function} is_island()

Returns True if the current Node instance has no parents or children (Node has degree 0).

:rtype: bool
```


```{py:function} path_exists_from(target_node, directional=True)

Checks whether there is a path from the target Node instance to the current Node instance.

:param Node target_node: The node to compare against
:param Node directional: (optional) if True, path searching operates normally (in leafward direction), if False search operates in both directions
:rtype: bool
```


```{py:function} path_exists_to(target_node, directional=True)

Checks whether there is a path from the current Node instance to the target Node instance.

:param Node target_node: The node to compare against
:param Node directional: (optional) if True, path searching operates normally (in leafward direction), if False search operates in both directions
:rtype: bool
```


```{py:function} is_ancestor_of(target_node, directional=True)

Checks whether the current Node instance is an ancestor of the provided target Node instance.

:param Node target_node: The node to compare against
:param Node directional: (optional) if True, path searching operates normally (in leafward direction), if False search operates in both directions
:rtype: bool
```


```{py:function} is_descendant_of(target_node, directional=True)

Checks whether the current Node instance is a descendant of the provided target Node instance.

:param Node target_node: The node to compare against
:param Node directional: (optional) if True, path searching operates normally (in leafward direction), if False search operates in both directions
:rtype: bool
```


```{py:function} is_sibling_of(target_node, directional=True)

Checks whether the current Node instance is a sibling of the provided target Node instance (see [terminology](../terminology)).

:param Node target_node: The node to compare against
:param Node directional: (optional) if True, path searching operates normally (in leafward direction), if False search operates in both directions
:rtype: bool
```


```{py:function} is_partner_of(target_node, directional=True)

Checks whether the current Node instance is a partner of the provided target Node instance (see [terminology](../terminology)).

:param Node target_node: The node to compare against
:param Node directional: (optional) if True, path searching operates normally (in leafward direction), if False search operates in both directions
:rtype: bool
```


### Methods returning other values


```{py:function} ancestor_count()

Returns the total number of ancestor Nodes.

:rtype: int
```


```{py:function} descendant_count()

Returns the total number of descendant Nodes.

:rtype: int
```


```{py:function} clan_count()

Returns the total number of clan Nodes.

:rtype: int
```


```{py:function} sibling_count()

Returns the total number of sibling Nodes.

:rtype: int
```


```{py:function} partner_count()

Returns the total number of partner Nodes.

:rtype: int
```


```{py:function} connected_graph_node_count()

Returns the count of all ancestors Nodes, self, and all descendant Nodes.

:rtype: int
```


```{py:function} node_depth()

Returns the depth of this Node instance from furthest root Node.

:rtype: int
```


```{py:function} distance(target_node)

Returns the shortest hops count to the target Node.

:param Node target_node: The node to compare against
:rtype: int
```


For future consideration:

- descendant_tree()
- ancestor_tree()


```{py:function} graphs()

A Node can be associated with multiple Graphs. This method returns a QuerySet of all Graph instances associated with the current Node.

:return: Graphs to which this Node belongs
:rtype: QuerySet
```
