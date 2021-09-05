from django.shortcuts import render

# Create your views here.
def sponsorus(request):
    return render(request, "sponsor_us/sponsors.html")