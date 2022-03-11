from django.contrib import admin

from tests.example.airports.models import AirlineGraph, AirportNode, AirRouteEdge


class AirRouteEdgesFKInline(admin.TabularInline):
    model = AirRouteEdge
    readonly_fields = (
        "parent",
        "child",
        "weight",
    )
    extra = 0


class AirRouteEdgesParentInline(admin.TabularInline):
    model = AirRouteEdge
    readonly_fields = (
        "graph",
        "parent",
        "child",
        "weight",
    )
    fk_name = "child"
    extra = 0


class AirRouteEdgesChildInline(admin.TabularInline):
    model = AirRouteEdge
    readonly_fields = (
        "graph",
        "parent",
        "child",
        "weight",
    )
    fk_name = "parent"
    extra = 0


@admin.register(AirlineGraph)
class AirlineGraphAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "iata",
        "icao",
        "callsign",
    ]
    inlines = (AirRouteEdgesFKInline,)


@admin.register(AirportNode)
class AirportNodeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "city",
        "country",
    ]
    inlines = (
        AirRouteEdgesParentInline,
        AirRouteEdgesChildInline,
    )


@admin.register(AirRouteEdge)
class AirRouteEdgeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "string_display",
        "graph",
        "parent",
        "child",
    ]
