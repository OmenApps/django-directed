"""Signals for django_directed."""
import django.dispatch


child_removed = django.dispatch.Signal()
child_added = django.dispatch.Signal()
