from django.urls import path
from sponsor_us.views import sponsorus

urlpatterns = [path("", sponsorus, name="sponsor_us")]