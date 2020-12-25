from django.shortcuts import render


def home(request):
    return render(request, "main/home.html")


def sponsor(request):
    return render(request, "main/sponsors.html")
