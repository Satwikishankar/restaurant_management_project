from django.shortcuts import render
from django.conf import settings

# Create your views here.

def homepage(request):
    return render(request, "homepage.html", {
        "restaurant_name": getattr(settings, "RESTAURANT_NAME", "My Restaurant")
    })

def custom_404(request, exception):
    return render(request, "404.html", status=404)