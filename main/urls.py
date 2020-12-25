from django.urls import path
from main.views import home, sponsor


urlpatterns = [
    path("", home, name="home"),
    path("why-sponsor-us/", sponsor, name="sponsor"),
]
