from django.shortcuts import render

# Create your views here.
def sponsor_us(request):
    return render(request, "sponsor_us/sponsors.html")