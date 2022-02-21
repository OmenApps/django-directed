# Terminology and Definitions

Learning to use graphs can be challenging because some concepts have multiple equivalent or similar terms and definitions. For instance, the words 'node' and 'vertex' typically mean the same thing, but some industries or fields may prefer one to the other.

To help clarify what is meant throughout this project, we define the following terms and definitions.

## Node

Here, `A` is a *node*. Another equivalent name for *node* that you may sometimes hear is *vertex*. While they are interchangeable, we will use the term *node* (or *nodes* for plural) exclusively within this project for consistency.

```{mermaid}
graph TD;
    A((A));

    style A fill:green,stroke:#333,stroke-width:4px;
```

## Edge

Here, `e` is an *edge* in the graph between nodes `A` and `B`. Edges connect nodes, and are directed (denoted here with an arrowhead). Edges are also called *lines*, *links*, *arcs*, or *arrows*. For consistency, this project will always use the term *edge* (or *edges* for plural).

```{mermaid}
graph TD;
    A((A));
    B((B));
    
    A--e-->B;

    linkStyle 0 stroke-width:3px,fill:none,stroke:green;
```

## Root

Here, Node A is the *root* of the graph. It has an in-degree (number of edges coming 'in') of 0.

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

Some types of graphs may have multiple roots. Here, Nodes `A` and `B` are *roots* of the graph. Again, if the in-degree is 0, the node is a root.

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

Here, Nodes `D` and `e` are *leaves* in the graph. They both have an out-degree (number of edges 'out' of the node) of 0.

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

## Island

In a given Graph, an *island* is a node with no parents nor children. Islands have an in-degree of 0 *and* and out-degree of 0. Here, node `E` is an island. There are no edges connecting it to any other node.

*(Note, there is no equivalent for edges. Every edge connects two [or in special cases, more] nodes.)*

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    D((D));
    E((E));
    
    A-->B; %% 0
    A-->C; %% 1
    B-->D; %% 2
    C-->D; %% 3

    style E fill:green,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
```

## Parent / Parents

Here, node `A` is the *parent* of node `B`, and node `B` is the *parent* of node `C`. Depending on the type of graph, nodes may have zero, one, or multiple parents.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    
    A-->B;
    B-->C;

    style A fill:#20961d,stroke:#333,stroke-width:4px;
    style B fill:#bdad01,stroke:#333,stroke-width:4px;
    style C fill:#f86f06,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
```

## Child / Children

Here, node `B` is a *child* of node `A`, and node `C` is a *child* of node `B`. Depending on the type of graph, nodes may have zero, one, or multiple children.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    
    A-->B;
    B-->C;

    style A fill:#f86f06,stroke:#333,stroke-width:4px;
    style B fill:#bdad01,stroke:#333,stroke-width:4px;
    style C fill:#20961d,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
```

## Ancestors

All nodes in connected paths in a rootward direction.

In this example, the *ancestors* for node `I` are nodes `A`, `C`, `E`, and `F`.

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
    
    A-->B; %% 0
    A-->C; %% 1
    B-->D; %% 2
    C-->D; %% 3
    A-->E; %% 4
    C-->F; %% 5
    E-->F; %% 6
    D-->G; %% 7
    G-->H; %% 8
    F-->H; %% 9
    F-->I; %% 10
    E-->J; %% 11
    J-->K; %% 12

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

All nodes in connected paths in a leafward direction.

In this example, the *descendants* for node `C` are nodes `D`, `F`, `G`, `H`, and `I`.

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
    
    A-->B; %% 0
    A-->C; %% 1
    B-->D; %% 2
    C-->D; %% 3
    A-->E; %% 4
    C-->F; %% 5
    E-->F; %% 6
    D-->G; %% 7
    G-->H; %% 8
    F-->H; %% 9
    F-->I; %% 10
    E-->J; %% 11
    J-->K; %% 12

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

The clan of a node includes all ancestor nodes, the node itself, and all descendant nodes.

In this example, the *clan* for node `F` includes nodes `A`, `C`, `E`, `H`, and `I`.

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
    
    A-->B; %% 0
    A-->C; %% 1
    B-->D; %% 2
    C-->D; %% 3
    A-->E; %% 4
    C-->F; %% 5
    E-->F; %% 6
    D-->G; %% 7
    G-->H; %% 8
    F-->H; %% 9
    F-->I; %% 10
    E-->J; %% 11
    J-->K; %% 12

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

In this example, the *siblings* of node `C` are nodes `B`, and `E`, because they all have node `A` in common as a parent.

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
    
    A-->B; %% 0
    A-->C; %% 1
    B-->D; %% 2
    C-->D; %% 3
    A-->E; %% 4
    C-->F; %% 5
    E-->F; %% 6
    D-->G; %% 7
    G-->H; %% 8
    F-->H; %% 9
    F-->I; %% 10
    E-->J; %% 11
    J-->K; %% 12

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

In this example, the *partners* of node `C` are nodes `B`, and `E`, because nodes `B` and `C` share node `D` as a child, and nodes `C` and `E` share node `F` as a child.

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
    
    A-->B; %% 0
    A-->C; %% 1
    B-->D; %% 2
    C-->D; %% 3
    A-->E; %% 4
    C-->F; %% 5
    E-->F; %% 6
    D-->G; %% 7
    G-->H; %% 8
    F-->H; %% 9
    F-->I; %% 10
    E-->J; %% 11
    J-->K; %% 12

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

The shortest number of hops from one node to a target node. The *distance* between node `C` and node `H` is 2. This is because the path from `C` to `F` to `H` involves 2 edges.

There is another path from `C` to `H` through nodes `D` and `G`, but that path is longer (3 edges), and when we refer to *distance* in this project, we always mean the smallest number of hops.

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
    
    A-->B; %% 0
    A-->C; %% 1
    B-->D; %% 2
    C--1-->D; %% 3
    A-->E; %% 4
    C--1-->F; %% 5
    E-->F; %% 6
    D--2-->G; %% 7
    G--3-->H; %% 8
    F--2-->H; %% 9
    F-->I; %% 10
    E-->J; %% 11
    J-->K; %% 12

    style C fill:green,stroke:#333,stroke-width:4px;
    style F fill:#f86f06,stroke:#333,stroke-width:4px;
    style H fill:green,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
    linkStyle 5 stroke-width:3px,fill:none,stroke:green;
    linkStyle 9 stroke-width:3px,fill:none,stroke:green;
```

## Node Depth

The distance of the node from furthest root in the graph. Because this can be a bit challenging to visualize, a few examples are provided below.

Because node `A` is the highest (and only) root in the following graph, its *node depth* is 0.


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
    
    A-->B; %% 0
    A-->C; %% 1
    B-->D; %% 2
    C-->D; %% 3
    A-->E; %% 4
    C-->F; %% 5
    E-->F; %% 6
    D-->G; %% 7
    G-->H; %% 8
    F-->H; %% 9
    F-->I; %% 10
    E-->J; %% 11
    J-->K; %% 12

    style A fill:green,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
```

Using the same graph as before, consider the depth of node `H`. There is only a single root (node `A`) in this graph, and the distance between node `A` and node `H` is 3. So the *node depth* of node `H` is 3.

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
    
    A-->B; %% 0
    A--1-->C; %% 1
    B-->D; %% 2
    C-->D; %% 3
    A-->E; %% 4
    C--2-->F; %% 5
    E-->F; %% 6
    D-->G; %% 7
    G-->H; %% 8
    F--3-->H; %% 9
    F-->I; %% 10
    E-->J; %% 11
    J-->K; %% 12

    style A fill:green,stroke:#333,stroke-width:4px;
    style C fill:#f86f06,stroke:#333,stroke-width:4px;
    style F fill:#f86f06,stroke:#333,stroke-width:4px;
    style H fill:green,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
    linkStyle 1 stroke-width:3px,fill:none,stroke:green;
    linkStyle 5 stroke-width:3px,fill:none,stroke:green;
    linkStyle 9 stroke-width:3px,fill:none,stroke:green;
```

Finally, we will look at a more complicated example with multiple roots at different levels. Here we want the *node depth* of node `F`.

While both nodes `A` and `D` are roots in this graph (they have in-degree of 0), node `A` has a greater distance from node `F`, so we determine the depth of node `F` from the viewpoint of node `A`. It takes 3 hops to reach node `F` from node `A`, so the *node depth* of node `F` is 3.

```{mermaid}
graph TD;
    A((A));
    B((B));
    C((C));
    D((D));
    E((E));
    F((F));
    
    A--1-->B; %% 0
    B--2-->C; %% 1
    D-->E; %% 2
    E-->F; %% 3
    C--3-->F; %% 4

    style A fill:green,stroke:#333,stroke-width:4px;
    style B fill:#f86f06,stroke:#333,stroke-width:4px;
    style C fill:#f86f06,stroke:#333,stroke-width:4px;
    style F fill:green,stroke:#333,stroke-width:4px;

    linkStyle default fill:none,stroke:gray
    linkStyle 0 stroke-width:3px,fill:none,stroke:green;
    linkStyle 1 stroke-width:3px,fill:none,stroke:green;
    linkStyle 4 stroke-width:3px,fill:none,stroke:green;
```
