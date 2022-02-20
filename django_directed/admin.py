from django.contrib import admin

from .models import (
    Edge,
    Node,
)


@admin.register(Edge)
class EdgeAdmin(admin.ModelAdmin):
    pass


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    pass
