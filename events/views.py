from django.shortcuts import render


def events(request):
    return render(request, "events/events.html")