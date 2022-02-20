from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView,
)

from .models import (
    Edge,
    Node,
)


class EdgeCreateView(CreateView):

    model = Edge


class EdgeDeleteView(DeleteView):

    model = Edge


class EdgeDetailView(DetailView):

    model = Edge


class EdgeUpdateView(UpdateView):

    model = Edge


class EdgeListView(ListView):

    model = Edge


class NodeCreateView(CreateView):

    model = Node


class NodeDeleteView(DeleteView):

    model = Node


class NodeDetailView(DetailView):

    model = Node


class NodeUpdateView(UpdateView):

    model = Node


class NodeListView(ListView):

    model = Node
