from django.urls import path
from members.views import alumni, team


urlpatterns = [path("alumni/", alumni, name="alumni"), path("team/", team, name="team")]
