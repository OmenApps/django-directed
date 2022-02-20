from django.urls import path
from django.views.generic import TemplateView

from . import views


app_name = "django_directed"
urlpatterns = [
    path(
        "Edge/~create/",
        views.EdgeCreateView.as_view(),
        name="Edge_create",
    ),
    path(
        "Edge/<int:pk>/~delete/",
        views.EdgeDeleteView.as_view(),
        name="Edge_delete",
    ),
    path(
        "Edge/<int:pk>/",
        views.EdgeDetailView.as_view(),
        name="Edge_detail",
    ),
    path(
        "Edge/<int:pk>/~update/",
        views.EdgeUpdateView.as_view(),
        name="Edge_update",
    ),
    path(
        "Edge/",
        views.EdgeListView.as_view(),
        name="Edge_list",
    ),
    path(
        "Node/~create/",
        views.NodeCreateView.as_view(),
        name="Node_create",
    ),
    path(
        "Node/<int:pk>/~delete/",
        views.NodeDeleteView.as_view(),
        name="Node_delete",
    ),
    path(
        "Node/<int:pk>/",
        views.NodeDetailView.as_view(),
        name="Node_detail",
    ),
    path(
        "Node/<int:pk>/~update/",
        views.NodeUpdateView.as_view(),
        name="Node_update",
    ),
    path(
        "Node/",
        views.NodeListView.as_view(),
        name="Node_list",
    ),
]
