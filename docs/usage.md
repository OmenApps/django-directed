# Usage

To use django-directed in a project, once installed via pip...

---

Internally, django-directed uses a combination of factories and abstract models, which makes possible:

- Composition of graph model sets with limited repetition of code
- Registering base model types for use with other project and in django-directed-admin
- Passing a standardized configuration object to the factory to change model functionality

Within a Django project utilizing django-directed the graph, edges, and nodes are represented as distinct concrete models, and multiple types of graphs can be built within the same project. These three work together to provide a consolidated API for working with graphs.

- a Graph model (extended from BaseGraph and then AbstractGraph)
- an Edge model (extended from BaseEdge and then AbstractEdge)
- a Node model (extended from BaseNode and then AbstractNode)

```{mermaid}
erDiagram
    Graph {
        any id
    }
    Node {
        ManyToManyField children
    }
    Edge {
        Graph id PK
        Node parent FK "parent Node"
        Node child FK "child Node"
    }

    Graph ||--o{ Edge : ""
    Node ||--o{ Edge : parent
    Node ||--o{ Edge : child
    Node }|--|{ Node : "M2M through Edge"
```

The connected graph is defined by the Edges associated with a Graph instance. This does mean an additional join on the Gaph table, but for typical use-cases the ratio of Graph instances to those of Nodes and Edges is tiny.
