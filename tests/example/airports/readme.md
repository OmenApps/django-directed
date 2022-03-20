# Example app: Airports

An app demonstrating one method of working with multidimensional graphs to model airports with a common set of nodes, and edges for each of the connecting airlines.

## Background

The app uses a Directed Cyclic Graphs to represent a number of european airlines, airports, and air routes.

- **Airlines** -> **Graph** model instances
- **Airports** -> **Node** model instances (shared between multiple graphs, since a given airport can service multiple airlines)
- **Air Routes** -> **Edge** model instances (specific to single graph, since airlines each have their own distinct air routes, even if they might sometimes depart from and arrive at the same airports as another airline)

## Scope & Goals

WIP