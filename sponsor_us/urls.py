from django.urls import path
from sponsor_us.views import sponsor_us

urlpatterns = [path("", sponsor_us, name="sponsor_us")]