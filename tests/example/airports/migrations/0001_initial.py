# Generated by Django 4.0.2 on 2022-03-11 03:33

import django.db.models.deletion
from django.db import migrations, models

import django_directed.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AirlineGraph",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("iata", models.CharField(max_length=2)),
                ("icao", models.CharField(max_length=3)),
                ("callsign", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Airline (Graph)",
                "verbose_name_plural": "Airlines (Graphs)",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="AirportNode",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("weight", models.SmallIntegerField(default=1)),
            ],
            options={
                "verbose_name": "Airport (Node)",
                "verbose_name_plural": "Airports (Nodes)",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="AirRouteEdge",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("weight", models.SmallIntegerField(default=1)),
                (
                    "child",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="parent_edges",
                        to="airports.airportnode",
                    ),
                ),
                (
                    "graph",
                    django_directed.fields.CurrentGraphFKField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="graph_edges",
                        related_query_name="graph_edges",
                        to="airports.airlinegraph",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="child_edges",
                        to="airports.airportnode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Air Route (Edge)",
                "verbose_name_plural": "Air Routes (Edges)",
                "ordering": ["parent__name"],
            },
        ),
        migrations.AddField(
            model_name="airportnode",
            name="children",
            field=models.ManyToManyField(
                blank=True, related_name="parents", through="airports.AirRouteEdge", to="airports.AirportNode"
            ),
        ),
    ]