from django.urls import path
from main.views import home, sponser


urlpatterns = [
    path("", home, name="home"),
    path("why-sponser-us/", sponser, name="sponsers"),
]
