from django.urls import path
from gallery.views import gallery


urlpatterns = [path("", gallery, name="gallery")]
