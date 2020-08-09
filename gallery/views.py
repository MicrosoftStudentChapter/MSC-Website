from django.shortcuts import render


def gallery(request):
    return render(request, "gallery/gallery.html")
