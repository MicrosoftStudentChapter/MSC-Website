from django.shortcuts import render


def alumni(request):
    return render(request, "members/alumni.html")


def team(request):
    return render(request, "members/team.html")
