from django.urls import path
from .views import projects


urlpatterns = [
    path("", projects, name="projects")
]