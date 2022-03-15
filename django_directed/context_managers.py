import logging
from contextlib import contextmanager

from django.db import models

from django_directed.models.abstract_base_models import BaseGraph

try:
    from asgiref.local import Local as local
except ImportError:
    from threading import local

logger = logging.getLogger("django_directed")

_threadlocals = local()


def _set_current_graph_instance(graph_fullname, current_graph_instance):
    """Sets the graph in the local thread"""
    setattr(_threadlocals, graph_fullname, current_graph_instance)


def get_current_graph_instance(graph_fullname):
    """Returns the graph if it exists in the local thread"""
    current_graph_instance = getattr(_threadlocals, graph_fullname, None)
    return current_graph_instance


@contextmanager
def graph_scope(graph):
    """
    Context manager for graphs. Used to set and cleanup Graph instance.
      If nested, saves outer context and resets it at conclusion of scope.

    `value` should be Graph instance.

    graph = MyGraphModel.objects.get(pk=1)

    Using the context context manager:
    ```python
    with graph_scope(graph):
        Profile.objects.get(pk=1)
    ```
    Using it as a decorator
    ```python
    @graph_scope(graph)
    def foo():
        Profile.object.get(pk=1)
    ```
    Using it in a task
    ```python
    def graph_do_some_task(graph_instance=None):
        with graph_scope(graph_instance):
            work()
    ```
    """

    if not isinstance(graph, BaseGraph):
        raise Exception("Wrong Graph type provided to graph_scope")

    graph_fullname = f"{graph._meta.app_label}.{graph._meta.label}"

    previous = getattr(_threadlocals, graph_fullname, None)
    _set_current_graph_instance(graph_fullname=graph_fullname, current_graph_instance=graph)

    try:
        yield
    finally:
        if previous is not None:
            _set_current_graph_instance(graph_fullname=graph_fullname, current_graph_instance=previous)
        else:
            delattr(_threadlocals, graph_fullname)
