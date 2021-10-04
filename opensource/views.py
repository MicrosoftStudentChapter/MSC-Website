from django.shortcuts import render


def opensource(request):
    return render(request, "opensource/opensource.html")
