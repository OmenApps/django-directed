import csv
import os

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from tests.example.airports.models import AirlineGraph, AirportNode


class Command(BaseCommand):
    help = "Inserts Data for the airports app"

    def handle(self, *args, **options):
        start_time = timezone.now()
        base_path = "./tests/example/airports/dataset"

        node_file_path = f"{base_path}/airports.csv"
        graph_file_path = f"{base_path}/airlines.csv"
        edge_file_path = f"{base_path}/routes.csv"

        graph_count = 0
        node_count = 0
        edge_count = 0

        # Create the Airports (Nodes)
        with open(node_file_path, "r") as node_csv_file:
            node_data = csv.reader(node_csv_file, delimiter=",")
            next(node_data)  # Skip top line
            airports = []
            for node_row in node_data:

                airport = AirportNode(
                    id=node_row[0],
                    name=node_row[1],
                    city=node_row[2],
                    country=node_row[3],
                )
                airports.append(airport)

            if airports:
                AirportNode.objects.bulk_create(airports)
                node_count = len(airports)
                print(f"Inserted {node_count} Airports")
            else:
                print("No Airports found")

        # Create the Airline (Graph) instances
        with open(graph_file_path, "r") as graph_csv_file:
            graph_data = csv.reader(graph_csv_file, delimiter=",")
            next(graph_data)  # Skip top line
            airlines = []
            for graph_row in graph_data:

                graph_id = int(graph_row[0])
                graph_name = graph_row[1]
                graph_iata = graph_row[2]
                graph_icao = graph_row[3]
                graph_callsign = graph_row[4]

                airline = AirlineGraph(
                    id=graph_id,
                    name=graph_name,
                    iata=graph_iata,
                    icao=graph_icao,
                    callsign=graph_callsign,
                )
                airlines.append(airline)

            if airlines:
                AirlineGraph.objects.bulk_create(airlines)
                graph_count = len(airlines)
                print(f"Inserted {graph_count} Airlines")
            else:
                print("No Airlines found")

        # Create the Air Routes (Edges) between Airports (Nodes) for each Airline (Graph)
        with open(edge_file_path, "r") as edge_csv_file:
            edge_data = csv.reader(edge_csv_file, delimiter=",")
            next(edge_data)  # Skip top line
            air_routes = []

            for edge_row in edge_data:
                route_id = edge_row[0]
                graph_id = edge_row[1]
                parent_id = edge_row[2]
                child_id = edge_row[3]

                air_route = AirportNode.children.through(
                    id=route_id,
                    graph_id=graph_id,
                    parent_id=parent_id,
                    child_id=child_id,
                )
                air_routes.append(air_route)

            if air_routes:
                AirportNode.children.through.objects.bulk_create(air_routes, batch_size=500, ignore_conflicts=True)
                edge_count = len(air_routes)
                print(f"Inserted {edge_count} Air Routes")
            else:
                print("No valid Air Routes found")

        # Cleanup unconnected / empty elements
        deleted_graphs = AirlineGraph.objects.filter(graph_edges__isnull=True).delete()
        deleted_nodes = AirportNode.objects.filter(children__isnull=True, parents__isnull=True).delete()

        print(f"Deleted unconnected nodes (Airports): {deleted_nodes}")
        print(f"Deleted empty graphs (Airlines): {deleted_graphs}")

        print("\nFinal counts:")
        print(f"\tAirports: {node_count - deleted_nodes[0]}")
        print(f"\tAirlines: {graph_count - deleted_graphs[0]}")
        print(f"\tAir Routes: {edge_count}")

        end_time = timezone.now()
        self.stdout.write(self.style.SUCCESS(f"Loading CSVs took: {(end_time - start_time).total_seconds()} seconds."))
