from django.core.management.base import BaseCommand
from django.utils import timezone

from tests.example.airports.models import AirlineGraph, AirportNode, AirRouteEdge


class Command(BaseCommand):
    help = "Inserts Data for the airports app"

    def handle(self, *args, **options):
        start_time = timezone.now()

        AirRouteEdge.objects.all().delete()
        AirlineGraph.objects.all().delete()
        AirportNode.objects.all().delete()

        end_time = timezone.now()
        self.stdout.write(self.style.SUCCESS(f"Deleting data took: {(end_time-start_time).total_seconds()} seconds."))
