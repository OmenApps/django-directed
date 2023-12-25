from __future__ import annotations

from typing import TYPE_CHECKING

import logging
from contextlib import contextmanager


try:
    from asgiref.local import Local as local
except ImportError:
    from threading import local

logger = logging.getLogger("django_directed")

_threadlocals = local()

if TYPE_CHECKING:
    from django_directed.models.abstract_base_graph_models import BaseGraph


def _set_current_graph_instance(graph_fullname, current_graph_instance):
    """Sets the graph in the local thread."""
    setattr(_threadlocals, graph_fullname, current_graph_instance)


def get_current_graph_instance(graph_fullname):
    """Returns the graph if it exists in the local thread."""
    current_graph_instance = getattr(_threadlocals, graph_fullname, None)
    return current_graph_instance


@contextmanager
def graph_scope(graph: BaseGraph):
    """Context manager for graphs.

    Used to set and cleanup Graph instance. If nested, saves outer context and resets it at conclusion of scope.

    <sphinx-skip>:

    Using the context manager:

    ```python
    graph = MyGraphModel.objects.get(pk=1)

    with graph_scope(graph):
        Profile.objects.get(pk=1)
    ```

    Using it as a decorator:

    ```python
    @graph_scope(graph)
    def foo():
        Profile.object.get(pk=1)
    ```

    Using it in a task:

    ```python
    def graph_do_some_task(graph_instance=None):
        with graph_scope(graph_instance):
            work()
    ```
    <sphinx-skip>
    """
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
