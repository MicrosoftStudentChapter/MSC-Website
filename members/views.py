from django.shortcuts import render
from .teamMembers import Secretaries, JointSecretaries, Heads


def alumni(request):
    return render(request, "members/alumni.html")


def team(request):

    sec = Secretaries()
    jsec = JointSecretaries()
    heads = Heads()

    return render(request, "members/about.html", context={'secretaries': sec, 'jointsec': jsec, 'heads': heads})
