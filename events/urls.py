from django.urls import path
from events.views import events


urlpatterns = [path("", events, name="events")]
