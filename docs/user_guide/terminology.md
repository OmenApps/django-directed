# Terminology and Definitions

Learning to use graphs can be challenging because some concepts have multiple equivalent or similar terms and definitions. For instance, the words 'node' and 'vertex' typically mean the same thing, but some industries or fields may prefer one to the other.

To help clarify what is meant throughout this project, we define the following terms and definitions. We make heavy use of familial terms, which can help with mentally visualizing the concepts.

This document does is not intended as a course in general graph theory. A graph in the context of this project is made up of nodes which are connected by edges. Edges typically link two nodes _asymmetrically_ in all of the directed graphs within django-directed.

## Node

Here, `A` is a _node_. Another equivalent name for _node_ that you may sometimes hear is _vertex_. While they are interchangeable, we will use the term _node_ (or _nodes_ for plural) exclusively within this project for consistency.

```{mermaid}
graph TD;
    A((A));

    style A fill:green,stroke:#333,stroke-width:4px;
```

## Edge

Here, `e` is an _edge_ in the graph between nodes `A` and `B`. Edges connect nodes, and are directed (denoted here with an arrowhead). Edges are also called _lines_, _links_, _arcs_, or _arrows_. For consistency, this project will always use the term _edge_ (or _edges_ for plural).

```{mermaid}
graph TD;
    A((A));
    B((B));

    A--e-->B;

    linkStyle 0 stroke-width:3px,fill:none,stroke:green;
```

## Root

Here, Node A is the _root_ of the graph. It has an in-degree (number of edges coming 'in') of 0.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    D((D));

    A-->B;
    A-->C;
    B-->D;
    C-->D;

    style A fill:green,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
```

## Roots

Some types of graphs may have multiple roots. Here, Nodes `A` and `B` are _roots_ of the graph. Again, if the in-degree is 0, the node is a root.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    D((D));

    A-->C;
    B-->C;
    B-->D;
    C-->D;

    style A fill:green,stroke:#333,stroke-width:4px;
    style B fill:green,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
```

## Leaf / Leaves

Here, Nodes `D` and `e` are _leaves_ in the graph. They both have an out-degree (number of edges 'out' of the node) of 0.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    D((D));
    E((E));

    A-->B;
    A-->C;
    B-->D;
    C-->D;
    A-->E;

    style D fill:green,stroke:#333,stroke-width:4px;
    style E fill:green,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
```

## Orphan

In a given Graph, an _orphan_ is a node with no parents nor children. Orphans have an in-degree of 0 _and_ and out-degree of 0. Here, node `E` is an orphan. There are no edges connecting it to any other node.

_(Note, there is no equivalent for edges. Every edge connects two [or in special cases, more] nodes.)_

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    D((D));
    E((E));

    %% 0
    A-->B;

    %% 1
    A-->C;

    %% 2
    B-->D;

    %% 3
    C-->D;

    style E fill:green,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
```

## Parent / Parents

The _parents_ for a given node _x_, if any exist, are those nodes which have a directed edge 'in' to node _x_. In graph theory, this may be refered to as a direct predecessor.

Here, node `A` is a _parent_ of node `B`, and node `B` is a _parent_ of node `C`. Depending on the type of graph, nodes may have zero, one, or multiple parents.

We also refer to _parent edges_, which are the directed edges themselves which point to the node. In this example, edge `e1` is a _parent edge_ of node `B`, and edge `e2` is a _parent edge_ of node `C`.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));

    A--e1-->B;
    B--e2-->C;

    style A fill:#20961d,stroke:#333,stroke-width:4px;
    style B fill:#bdad01,stroke:#333,stroke-width:4px;
    style C fill:#f86f06,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
```

## Child / Children

The _children_ for a given node _x_, if any exist, are those nodes which have a directed edge 'out' from node _x_. In graph theory, this may be refered to as a direct successor.

Here, node `B` is a _child_ of node `A`, and node `C` is a _child_ of node `B`. Depending on the type of graph, nodes may have zero, one, or multiple children.

We also refer to _children edges_, which are the directed edges themselves which point from the node. In this example, edge `e1` is a _child edge_ of node `A`, and edge `e2` is a _child edge_ of node `B`.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));

    A--e1-->B;
    B--e2-->C;

    style A fill:#f86f06,stroke:#333,stroke-width:4px;
    style B fill:#bdad01,stroke:#333,stroke-width:4px;
    style C fill:#20961d,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
```

## Ancestors

All nodes in connected paths in a rootward direction. In graph theory, this may be refered to as predecessors.

In this example, the _ancestors_ for node `I` are nodes `A`, `C`, `E`, and `F`.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    D((D));
    E((E));
    F((F));
    G((G));
    H((H));
    I((I));
    J((J));
    K((K));


    A-->B;
    A-->C;
    B-->D;
    C-->D;
    A-->E;
    C-->F;
    E-->F;
    D-->G;
    G-->H;
    F-->H;
    F-->I;
    E-->J;
    J-->K;

    style I fill:green,stroke:#333,stroke-width:4px;
    style A fill:#f86f06,stroke:#333,stroke-width:4px;
    style C fill:#f86f06,stroke:#333,stroke-width:4px;
    style F fill:#f86f06,stroke:#333,stroke-width:4px;
    style E fill:#f86f06,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
    linkStyle 1 stroke-width:3px,fill:none,stroke:green;
    linkStyle 4 stroke-width:3px,fill:none,stroke:green;
    linkStyle 5 stroke-width:3px,fill:none,stroke:green;
    linkStyle 6 stroke-width:3px,fill:none,stroke:green;
    linkStyle 10 stroke-width:3px,fill:none,stroke:green;
```

## Descendants

All nodes in connected paths in a leafward direction. In graph theory, this may be refered to as successors.

In this example, the _descendants_ for node `C` are nodes `D`, `F`, `G`, `H`, and `I`.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    D((D));
    E((E));
    F((F));
    G((G));
    H((H));
    I((I));
    J((J));
    K((K));

    A-->B;
    A-->C;
    B-->D;
    C-->D;
    A-->E;
    C-->F;
    E-->F;
    D-->G;
    G-->H;
    F-->H;
    F-->I;
    E-->J;
    J-->K;

    style C fill:green,stroke:#333,stroke-width:4px;
    style D fill:#f86f06,stroke:#333,stroke-width:4px;
    style F fill:#f86f06,stroke:#333,stroke-width:4px;
    style G fill:#f86f06,stroke:#333,stroke-width:4px;
    style H fill:#f86f06,stroke:#333,stroke-width:4px;
    style I fill:#f86f06,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
    linkStyle 3 stroke-width:3px,fill:none,stroke:green;
    linkStyle 5 stroke-width:3px,fill:none,stroke:green;
    linkStyle 7 stroke-width:3px,fill:none,stroke:green;
    linkStyle 8 stroke-width:3px,fill:none,stroke:green;
    linkStyle 9 stroke-width:3px,fill:none,stroke:green;
    linkStyle 10 stroke-width:3px,fill:none,stroke:green;
```

## Clan

The clan of a node includes all ancestor nodes, the node itself, and all descendant nodes. In graph theory, this can be refered to as the maximal paths through a given node.

In this example, the _clan_ for node `F` includes nodes `A`, `C`, `E`, `H`, and `I`.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    D((D));
    E((E));
    F((F));
    G((G));
    H((H));
    I((I));
    J((J));
    K((K));

    A-->B;
    A-->C;
    B-->D;
    C-->D;
    A-->E;
    C-->F;
    E-->F;
    D-->G;
    G-->H;
    F-->H;
    F-->I;
    E-->J;
    J-->K;

    style F fill:green,stroke:#333,stroke-width:4px;
    style A fill:#f86f06,stroke:#333,stroke-width:4px;
    style C fill:#f86f06,stroke:#333,stroke-width:4px;
    style E fill:#f86f06,stroke:#333,stroke-width:4px;
    style H fill:#f86f06,stroke:#333,stroke-width:4px;
    style I fill:#f86f06,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
    linkStyle 1 stroke-width:3px,fill:none,stroke:green;
    linkStyle 4 stroke-width:3px,fill:none,stroke:green;
    linkStyle 5 stroke-width:3px,fill:none,stroke:green;
    linkStyle 6 stroke-width:3px,fill:none,stroke:green;
    linkStyle 9 stroke-width:3px,fill:none,stroke:green;
    linkStyle 10 stroke-width:3px,fill:none,stroke:green;
```

## Siblings

All nodes that share a parent with this node, excluding the node itself.

In this example, the _siblings_ of node `C` are nodes `B`, and `E`, because they all have node `A` in common as a parent.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    D((D));
    E((E));
    F((F));
    G((G));
    H((H));
    I((I));
    J((J));
    K((K));

    A-->B;
    A-->C;
    B-->D;
    C-->D;
    A-->E;
    C-->F;
    E-->F;
    D-->G;
    G-->H;
    F-->H;
    F-->I;
    E-->J;
    J-->K;

    style C fill:green,stroke:#333,stroke-width:4px;
    style B fill:#f86f06,stroke:#333,stroke-width:4px;
    style E fill:#f86f06,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
    linkStyle 1 stroke-width:3px,fill:none,stroke:green;
    linkStyle 0 stroke-width:3px,fill:none,stroke:green;
    linkStyle 4 stroke-width:3px,fill:none,stroke:green;
```

## Partners

All nodes that share a child with this node, excluding the node itself.

In this example, the _partners_ of node `C` are nodes `B`, and `E`, because nodes `B` and `C` share node `D` as a child, and nodes `C` and `E` share node `F` as a child.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    D((D));
    E((E));
    F((F));
    G((G));
    H((H));
    I((I));
    J((J));
    K((K));

    A-->B;
    A-->C;
    B-->D;
    C-->D;
    A-->E;
    C-->F;
    E-->F;
    D-->G;
    G-->H;
    F-->H;
    F-->I;
    E-->J;
    J-->K;

    style C fill:green,stroke:#333,stroke-width:4px;
    style B fill:#f86f06,stroke:#333,stroke-width:4px;
    style E fill:#f86f06,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
    linkStyle 2 stroke-width:3px,fill:none,stroke:green;
    linkStyle 3 stroke-width:3px,fill:none,stroke:green;
    linkStyle 5 stroke-width:3px,fill:none,stroke:green;
    linkStyle 6 stroke-width:3px,fill:none,stroke:green;
```

## Distance

The shortest number of hops from one node to a target node. The _distance_ between node `C` and node `H` is 2. This is because the path from `C` to `F` to `H` involves 2 edges.

There is another path from `C` to `H` through nodes `D` and `G`, but that path is longer (3 edges), and when we refer to _distance_ in this project, we always mean the smallest number of hops.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C start));
    D((D));
    E((E));
    F((F));
    G((G));
    H((H end));
    I((I));
    J((J));
    K((K));

    A-->B;
    A-->C;
    B-->D;
    C--1-->D;
    A-->E;
    C--1-->F;
    E-->F;
    D--2-->G;
    G--3-->H;
    F--2-->H;
    F-->I;
    E-->J;
    J-->K;

    style C fill:green,stroke:#333,stroke-width:4px;
    style F fill:#f86f06,stroke:#333,stroke-width:4px;
    style H fill:green,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
    linkStyle 5 stroke-width:3px,fill:none,stroke:green;
    linkStyle 9 stroke-width:3px,fill:none,stroke:green;
```

## Node Depth

The distance of the node from furthest root in the graph. Because this can be a bit challenging to visualize, a few examples are provided below.

Because node `A` is the highest (and only) root in the following graph, its _node depth_ is 0.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    D((D));
    E((E));
    F((F));
    G((G));
    H((H));
    I((I));
    J((J));
    K((K));

    A-->B;
    A-->C;
    B-->D;
    C-->D;
    A-->E;
    C-->F;
    E-->F;
    D-->G;
    G-->H;
    F-->H;
    F-->I;
    E-->J;
    J-->K;

    style A fill:green,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
```

Using the same graph as before, consider the depth of node `H`. There is only a single root (node `A`) in this graph, and the distance between node `A` and node `H` is 3. So the _node depth_ of node `H` is 3.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    D((D));
    E((E));
    F((F));
    G((G));
    H((H));
    I((I));
    J((J));
    K((K));

    A-->B;
    A--1-->C;
    B-->D;
    C-->D;
    A-->E;
    C--2-->F;
    E-->F;
    D-->G;
    G-->H;
    F--3-->H;
    F-->I;
    E-->J;
    J-->K;

    style A fill:green,stroke:#333,stroke-width:4px;
    style C fill:#f86f06,stroke:#333,stroke-width:4px;
    style F fill:#f86f06,stroke:#333,stroke-width:4px;
    style H fill:green,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
    linkStyle 1 stroke-width:3px,fill:none,stroke:green;
    linkStyle 5 stroke-width:3px,fill:none,stroke:green;
    linkStyle 9 stroke-width:3px,fill:none,stroke:green;
```

Finally, we will look at a more complicated example with multiple roots at different levels. Here we want the _node depth_ of node `F`.

While both nodes `A` and `D` are roots in this graph (they have in-degree of 0), node `A` has a greater distance from node `F`, so we determine the depth of node `F` from the viewpoint of node `A`. It takes 3 hops to reach node `F` from node `A`, so the _node depth_ of node `F` is 3.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    D((D));
    E((E));
    F((F));

    A--1-->B;
    B--2-->C;
    D-->E;
    E-->F;
    C--3-->F;

    style A fill:green,stroke:#333,stroke-width:4px;
    style B fill:#f86f06,stroke:#333,stroke-width:4px;
    style C fill:#f86f06,stroke:#333,stroke-width:4px;
    style F fill:green,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
    linkStyle 0 stroke-width:3px,fill:none,stroke:green;
    linkStyle 1 stroke-width:3px,fill:none,stroke:green;
    linkStyle 4 stroke-width:3px,fill:none,stroke:green;
```
