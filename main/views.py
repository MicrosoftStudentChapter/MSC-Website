from django.shortcuts import render


def home(request):
    return render(request, "main/home.html")


def sponser(request):
    return render(request, "main/sponsers.html")
