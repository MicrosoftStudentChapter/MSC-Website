from django.urls import path
from opensource.views import opensource

urlpatterns = [path("", opensource, name="opensource")]
