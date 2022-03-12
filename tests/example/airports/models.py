from django.contrib import admin
from django.db import models

from django_directed.config import GraphConfig
from django_directed.models.model_factory import factory

my_config = GraphConfig(
    graph_fullname="airports.AirlineGraph",
    edge_fullname="airports.AirRouteEdge",
    node_fullname="airports.AirportNode",
)
cyclic = factory.create("CYCLIC", config=my_config)


class AirlineGraph(cyclic.graph()):
    # Airlines
    name = models.CharField(max_length=100)
    iata = models.CharField(max_length=2)
    icao = models.CharField(max_length=3)
    callsign = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Airline (Graph)"
        verbose_name_plural = "Airlines (Graphs)"
        ordering = ["name"]


class AirRouteEdge(cyclic.edge()):
    # Air Routes
    weight = models.SmallIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.parent.name} -to- {self.child.name}"

    class Meta:
        verbose_name = "Air Route (Edge)"
        verbose_name_plural = "Air Routes (Edges)"
        ordering = ["parent__name"]

    @admin.display(description="String Display")
    def string_display(self):
        return f"{self.__str__()}"


class AirportNode(cyclic.node()):
    # Airports
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    weight = models.SmallIntegerField(default=1)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Airport (Node)"
        verbose_name_plural = "Airports (Nodes)"
        ordering = ["name"]
