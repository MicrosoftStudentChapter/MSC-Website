from django.shortcuts import render
from .teamMembers import Secretaries, JointSecretaries


def alumni(request):
    return render(request, "members/alumni.html")


def team(request):
    # secretaries = {"Pranjal": Pranjal,
    #                "Arpit": Arpit}

    #details = secretaries.values()
    sec = Secretaries()
    jsec = JointSecretaries()

    return render(request, "members/about.html", context={'secretaries': sec, 'jointsec': jsec})

# ONLY FOR TESTING PURPOSE

# secretaries = {"Pranjal": {"name": "Pranjal", "post": "gen sec"},
#                "Arpit": {"name": "Arpit", "post": "Fin sec"}}

# for detail in secretaries.values():
#     print(detail["name"])
#     print(detail["post"])
