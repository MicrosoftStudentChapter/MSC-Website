from django.shortcuts import render
# from .teamMembers import Secretaries, JointSecretaries, Heads
from .teamMembers import members


def alumni(request):
    return render(request, "members/alumni.html")


def team(request):

    # sec = Secretaries()
    # jsec = JointSecretaries()
    # heads = Heads()

    secretaries = filter(
        lambda member: 'General Secretary' in member.position or 'Finance Secretary' in member.position, members)
    joint_secretaries = filter(
        lambda member: 'Joint Secretary' in member.position, members)
    heads = filter(
        lambda member: 'Head' in member.position, members)

    family = {"secretaries": secretaries,
              "joint_secretaries": joint_secretaries, "heads": heads}

    return render(request, "members/about.html", context={'members': family})
