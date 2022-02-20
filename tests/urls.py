from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("", include("django_directed.urls", namespace="django_directed")),
]
