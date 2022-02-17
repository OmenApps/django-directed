# django-directed

Tools for building, querying, manipulating, and exporting directed graphs with django

## Background

This project is the successor of another django package of mine, [django-postgresql-dag](https://pypi.org/project/django-postgresql-dag/), which itself was forked and heavily modified from [django-dag](https://pypi.org/project/django-dag/) and [django-dag-postgresql](https://pypi.org/project/django-dag-postgresql/).

When I started building django-postgresql-dag, I was rather new to a lot of concepts in both graph theory and database queries. As a result, I felt that I backed myself into corners in some ways with that earlier package. I developed django-postgresql-dag to serve as the underlying structure of an application that modeled real-world infrastructure as a directed acyclic graph, but I soon found that there were other graph-related things I wanted to be able to do that were not DAG-specific. Additionally, using CTE's in django has been somewhat democratized with the django-cte package and other changes over the years, and it might be feasible to port at least a portion of the graph functionality to database backends other than Postgres.

Some of the design decisions here:
- *A reasonable amount of flexibility* - The predecessor for this package was limited (in name and in some implementation aspects) solely to working with Directed Acyclic Graphs. But I find that I often need other types of directed graphs. This package should still do one thing well - working with directed graphs - but I've opened the scope a bit. There are a lot of commonalities between all types of directed graphs, so the package need not balloon to solve every graph situation or need. Directed graphs in general can solve or model an incredible number of real-world or web-related things.
- *Prioritize querying over writing* - For my typical purposes, quickly adding large graphs to the database is an uncommon task. Instead, in most graph applications I am either slowly adding a node here and there (comments, categories, etc), or I am adding large graphs in an asynchronous manner (uploading and building the graph of an entire physical infrastructure model from a CSV file). In either case, the speed at which the graph is written is of much less consequence than the ability to query the resulting graph quickly.
- *Include tools for modifying and reconfiguring graphs* - pre-processing (calculating graph hashes, etc), move or copy sections of a graph, insert and delete nodes, etc.

## Scope & Goals

This package should be complete enough to perform a majority of tasks needed for working with an assortment of directed graphs in django applications, but it should also be flexible and extensible enough to allow for customization and novel approaches to problems in practical graph application.

### Building Directed Graphs

The scope of this package includes working with a variety of directed graphs. This includes eventually supporting functionality for each of these types of directed graphs:

    Directed graphs aka DiGraphs
        Directed cyclic graph
        Directed acyclic graph (DAG)
            Polytree (or directed tree, oriented tree, or singly connected network) is a directed acyclic graph (DAG) whose underlying undirected graph is a tree
                Arborescence (or out-tree or rooted tree) (single-rooted polytree)
                    Directed binary tree
                    Directed quadtree
                    Directed octree

Other things to consider as a possibility:

    Multigraphs - the same pair of nodes may be connected by multiple edges. This might be further constrained in a cyclic graph to limit edges between two nodes to no more than two, with one edge in each direction.



### Querying Directed Graphs


### Manipulating Directed Graphs


### Exporting Directed Graphs


## Example use-cases

Graphs can be used to model an incredibly large range of ideas, physical systems, concepts, web-components, etc. Here is a very incomplete list of some of the ways you might use django-directed, along with the underlying structure that might be best to represent them.

- Threaded discussion comments
- Social "follows" (which users are following which)
- Model of resource flow in gas/electrical/water/sewer distribution systems
- The underlying structure to business process automation (e.g. tools like Airflow)
- Hierarchical bill of materials for a product
- Network mapping (Internet device map, map of linked pages in a website, modeling roadways, modeling airline/train paths, etc)
- Social graphs showing relationships between people
- Modeling dependencies in software applications
- Scheduling tasks for project management
- Fault-tree analysis in industrial systems
- Version control systems
- Which academic papers are cited by later papers
- Dependencies in educational plans (which pieces of knowledge or classes must preceed others as a student progresses toward a goal?)
- Modeling supply chains from resource XXX to manufacturer to retailer
- Family trees and other genealogical models
- Hierarchical file/folder structures
- Mind maps
- TRIE structures
- Storing information about phone calls, emails, or other interactions between people


Essentially, just about anything involving causal relationships, hierarchies, or dependencies can be modeled with a directed graph. This package may be useful if you need to persist that information for use with django applications.


## CHANGELOG

- 20210208
    - Building initial readme entry to start documenting project goals.
