from django.contrib import admin
from django.db import models

from django_directed.config import GraphConfig
from django_directed.models import directed_factory

my_config = GraphConfig(
    graph_type="CYCLIC",
    graph_fullname="airports.AirlineGraph",
    edge_fullname="airports.AirRouteEdge",
    node_fullname="airports.AirportNode",
)
cyclic = directed_factory.get(config=my_config)


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

    list_display = ("string_display",)

    def string_display(self):
        return f"{self.__str__()}"

    string_display.short_description = "String Display"


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
