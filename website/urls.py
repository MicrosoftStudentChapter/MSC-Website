from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("events/", include("events.urls")),
    path("gallery/", include("gallery.urls")),
    path("members/", include("members.urls")),
    path("projects/", include("projects.urls")),
]
