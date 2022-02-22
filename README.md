# django-directed

Tools for building, querying, manipulating, and exporting directed graphs with django.

Documentation can be found at https://django-directed.readthedocs.io/en/latest/

***Note**: This project is very much a Work In Progress, and is not production-ready.*

## Background

This project is the successor of another django package of mine, [django-postgresql-dag](https://pypi.org/project/django-postgresql-dag/), which itself was forked and heavily modified from [django-dag](https://pypi.org/project/django-dag/) and [django-dag-postgresql](https://pypi.org/project/django-dag-postgresql/).

When I started building django-postgresql-dag, I was rather new to a lot of concepts in both graph theory and database queries. As a result, I felt that I backed myself into corners in some ways with that earlier package. I developed django-postgresql-dag to serve as the underlying structure of an application that modeled real-world infrastructure as a directed acyclic graph, but I soon found that there were other graph-related things I wanted to be able to do that were not DAG-specific. Additionally, using CTE's in django has been somewhat democratized with the django-cte package and other changes over the years, and it might be feasible to port at least a portion of the graph functionality to database backends other than Postgres.

Some of the design decisions here:
- *A reasonable amount of flexibility* - The predecessor for this package was limited (in name and in some implementation aspects) solely to working with Directed Acyclic Graphs in Postgresql. I often find, though, that I need other types of directed graphs. This package should still do one thing well - working with directed graphs - but I've opened the scope a bit.
- *DRY* - There are a lot of commonalities between all types of directed graphs, so we should be able to model graphs of different types with a common API, extending when necessary to perform specialized tasks that do not apply to all graphs.
- *Prioritize querying over writing* - For my typical purposes, quickly adding large graphs to the database is an uncommon task. Instead, in most graph applications I am either slowly adding a node here and there (comments, categories, etc), or I am adding large graphs in an asynchronous manner (uploading and building the graph of an entire physical infrastructure model from a CSV file). In either case, the speed at which the graph is written is of much less consequence than the ability to query the resulting graph quickly.
- *Include tools for modifying and reconfiguring graphs* - move or copy subgraphs, insert and delete nodes, and pre-processing (calculating graph hashes or copying a subgraph with a function applied), etc.
- *Optimized for sparse graphs* - Most of the graph structures I find myself building and working with are sparse. There are generally few connections from each node to another. Said another way, the typical degree of the nodes is small (often no more than 5 or so). This seems pretty common for many real-world models such as physical infrastructure, as well as many common web & software related graph uses such as threaded comments, automation processes, and version control systems. If you are trying to model large, highly-connected graphs, this might not be the right package for you.

## Scope & Goals

Directed graphs in general can solve or model an incredible number of real-world or web-related problems and concepts. This package should be complete enough to perform a majority of tasks needed for working with an assortment of directed graphs in django applications, but it should also be flexible and extensible enough to allow for customization and novel approaches to problems in practical graph application.

### Building Directed Graphs

The scope of this package includes working with a variety of directed graphs. This includes eventually supporting functionality for each of these types of directed graphs:

- Directed graphs aka DiGraphs
  - Directed cyclic graph
  - Directed acyclic graph (DAG)
    - Polytree (aka directed tree, oriented tree, or singly connected network) - DAGs whose underlying undirected graph is a tree
      - Arborescence (or out-tree or rooted tree) (single-rooted polytree)

Other things to consider as a possibility (in suspected order of complexity):

- **Subclasses of Arborescence**
  - Directed binary tree
  - Directed quadtree
  - Directed octree
- **Binary Search Trees (BST)**
- **Multigraphs** - Grphs where the same pair of nodes may be connected by more than one edge.
  - This might be further constrained in a cyclic graph to limit edges between two nodes to no more than two, with one edge in each direction.
- **Hypergraphs** - Graphs where edges can join more than just two nodes.


For further details on building, querying, manipulating, and exporting graphs, please [Read the Docs](https://django-directed.readthedocs.io/en/latest/)


## Example Use-Cases of django-directed

Graphs can be used to model an incredibly large range of ideas, physical systems, concepts, web-components, etc. Here is a very incomplete list of some of the ways you might use django-directed, along with the underlying structure that might be best to represent them.

| Use-Cases                                                                                                                           | Potential Data Structure     |
| ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| Threaded discussion comments                                                                                                        | Arborescence                 |
| Social follows" (which users are following which)"                                                                                  | Directed cyclic graph        |
| Model of resource flow in gas/electrical/water/sewer distribution systems                                                           | Arborescence                 |
| The underlying structure to business process automation (e.g. tools like Airflow)                                                   | Directed cyclic graph or DAG |
| Hierarchical bill of materials for a product                                                                                        | Polytree or Arborescence     |
| Network mapping (Internet device map, map of linked pages in a website, modeling roadways, modeling airline/train paths, etc)       | Directed cyclic graph        |
| Modeling dependencies in software applications                                                                                      | DAG                          |
| Scheduling tasks for project management                                                                                             | Directed cyclic graph or DAG |
| Fault-tree analysis in industrial systems                                                                                           | Polytree                     |
| Version control systems                                                                                                             | DAG                          |
| Which academic papers are cited by later papers                                                                                     | DAG                          |
| Dependencies in educational plans (which pieces of knowledge or classes must preceed others as a student progresses toward a goal?) | Arborescence                 |
| Modeling supply chains from initial resource (mining, forestry, etc) to manufacturer to retailer to consumer market                 | DAG or Polytree              |
| Family trees and other genealogical models                                                                                          | DAG                          |
| Hierarchical file/folder structures                                                                                                 | Arborescence                 |
| Mind maps                                                                                                                           | DAG                          |
| TRIE structures                                                                                                                     | Arborescence                 |
| Customer journey maps                                                                                                               | DAG                          |
| Storing information about phone calls, emails, or other interactions between people                                                 | Directed cyclic graph or DAG |

Essentially, just about anything involving causal relationships, hierarchies, or dependencies can be modeled with a directed graph. This package may be useful if you need to persist that information for use with django applications.

## Why not use a graph database instead?

- Compatibility - Graph databases don't play very nicely with Django and the Django ORM. There are 3rd party packages to shoehorn in the required functionality, but django is designed for relational databases.
- Simplicity - If most of the work you are doing needs a relational database, mixing an additional database into the project might not be ideal.
- Tradeoffs - Graph databases are not a panacea. They bring their own set of pros and cons. Maybe a graph database is ideal for your project. But maybe you'll do just as well using django-directed. I encourage you to read up on the benefits graph databases bring, the issues they solve, and also the areas where they do not perform as well as a relational database.

## ToDo

- [ ] Write the code!
- [ ] Write documentation for ReadTheDocs
- [ ] Build example applications
