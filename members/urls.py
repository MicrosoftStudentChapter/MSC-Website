from django.urls import path
from members.views import team


urlpatterns = [
    # path("alumni/", alumni, name="alumni"),
    path("about/", team, name="about")
]
