import pytest
from django.conf import settings
from django.test import TestCase
from pytest_django.fixtures import django_assert_num_queries

from tests.example.airports.models import AirlineGraph, AirportNode


@pytest.mark.django_db
def test_airport_models(django_assert_num_queries):
    """Build and test a single basic directed cyclic graph"""

    airline = AirlineGraph.objects.create(name="Test Airport Name", iata="XY", icao="ABC", callsign="Test Callsign")

    assert airline.name == "Test Airport Name"
    assert airline.iata == "XY"
    assert airline.icao == "ABC"
    assert airline.callsign == "Test Callsign"

    assert AirlineGraph.objects.all().count() == 1

    # print(dir(AirportNode))

    with django_assert_num_queries(10) as captured:
        airport1 = AirportNode.objects.create(
            name="Airport Name 1", city="The City", country="The Country", weight=100
        )

        assert airport1.name == "Airport Name 1"
        assert airport1.city == "The City"
        assert airport1.country == "The Country"
        assert airport1.weight == 100

        airport2 = AirportNode.objects.create(
            name="Airport Name 2", city="Another City", country="The Country", weight=100
        )
        airport3 = AirportNode.objects.create(
            name="Airport Name 3", city="Another City", country="The Country", weight=50
        )
        airport4 = AirportNode.objects.create(name="Airport Name 4", city="The City", country="The Country", weight=50)
        airport5 = AirportNode.objects.create(name="Airport Name 5", city="The City", country="The Country", weight=50)
        airport6 = AirportNode.objects.create(
            name="Airport Name 6", city="The City", country="The Country", weight=100
        )
        airport7 = AirportNode.objects.create(
            name="Airport Name 7", city="The City", country="The Country", weight=100
        )
        airport8 = AirportNode.objects.create(
            name="Airport Name 8", city="The City", country="The Country", weight=100
        )
        airport9 = AirportNode.objects.create(
            name="Airport Name 9", city="The City", country="The Country", weight=100
        )
        airport10 = AirportNode.objects.create(
            name="Airport Name 10", city="The City", country="The Country", weight=100
        )

    # Check that nodes were created as expected
    assert "Airport Name 1" in captured.captured_queries[0]["sql"]
    assert "Airport Name 10" in captured.captured_queries[9]["sql"]

    edge_1_to_2 = airport1.add_child(child=airport2)

    # Check that edge was created correctly
    # Expecting:
    #    parent  ->     edge    ->  child
    #   airport1 -> edge_1_to_2 -> airport2
    assert edge_1_to_2.parent == airport1
    assert edge_1_to_2.child == airport2
    assert airport2 in airport1.children.all()
    assert airport2 not in airport1.parents.all()
    assert airport1 in airport2.parents.all()
    assert airport1 not in airport2.children.all()
    assert airport2 in airport1.descendants()
    assert airport1.descendants_count() == 1

    children = AirportNode.objects.filter(weight=50)  # Airports 3, 4, and 5
    airport2_edges = airport2.add_children(children=children)
    assert len(airport2_edges) == 3
    assert airport2_edges[0].parent == airport2
    assert airport2_edges[1].parent == airport2
    assert airport2_edges[2].parent == airport2
    assert any(
        [
            airport2_edges[0].child == airport3,
            airport2_edges[0].child == airport4,
            airport2_edges[0].child == airport5,
        ]
    )
    assert any(
        [
            airport2_edges[0].child == airport3,
            airport2_edges[1].child == airport4,
            airport2_edges[2].child == airport5,
        ]
    )
    assert any(
        [
            airport2_edges[0].child == airport3,
            airport2_edges[1].child == airport4,
            airport2_edges[2].child == airport5,
        ]
    )

    edge_6_to_3 = airport6.add_parent(airport3)

    parents = AirportNode.objects.filter(city="Another City")  # Airports 2 and 3
    airport7.add_parents(parents=parents)
    airport8.add_parents(parents=parents)

    # Check that airport7 and airport8 share the same parents
    assert airport7.parents.count() == airport8.parents.count() == 2
    assert airport2 in airport7.parents.all()
    assert airport2 in airport8.parents.all()
    assert airport3 in airport7.parents.all()
    assert airport3 in airport8.parents.all()
    assert airport7 in airport2.children.all()
    assert airport8 in airport2.children.all()
    assert airport7 in airport3.children.all()
    assert airport8 in airport3.children.all()

    edge_8_to_9 = airport8.add_child(child=airport9)
    edge_8_to_10 = airport8.add_child(child=airport10)

    # Check that edge_8_to_9 and edge_8_to_10 share a parent, but not a child
    assert edge_8_to_9.parent == edge_8_to_10.parent
    assert not edge_8_to_9.child == edge_8_to_10.child
    assert airport9.parents.first() == airport10.parents.first()
    assert edge_8_to_9.parent == airport9.parents.first()
    assert edge_8_to_9.parent == airport10.parents.first()
    assert edge_8_to_10.parent == airport9.parents.first()
    assert edge_8_to_10.parent == airport10.parents.first()
    assert edge_8_to_9.child in airport8.children.all()
    assert edge_8_to_10.child in airport8.children.all()

    # Check characteristics related to airport1
    assert airport1.parents.count() == 0
    assert airport1.children.count() == 1
    assert airport1.children.first() == airport2
    assert airport1.descendants_count() == 9  # All the other airports are descendants
    assert airport1.children.first().parents.first() == airport1  # airport1's child's parent is airport1


@pytest.mark.django_db
def test_airport_data():
    """Load fixture data, and test the multi-dimensional aspects of the Graphs"""
    pass
