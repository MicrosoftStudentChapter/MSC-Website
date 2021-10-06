from django.urls import path
from main.views import home

urlpatterns = [
    path("", home, name="home"),
]
