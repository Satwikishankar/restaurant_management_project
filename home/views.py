from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuItem
from .forms import ContactForm
# Create your views here.


def homepage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")

        else:
            form = ContactForm()

    return render(request, "homepage.html", {
        "restaurant_name": settings.RESTAURANT_NAME,
        "restaurant_address": getattr(settings, "RESTAURANT_ADDRESS", "123 Main Street, Vijayawada, India"),
        "form": form
    })

def custom_404(request, exception):
    return render(request, "404.html", status=404)

def home(request):
    return render(request, "about.html", {
        "phone_number": settings.RESTAURANT_PHONE
    })

def menu(request):
    items = MenuItem.objects.all()
    return render(request, "menu.html", {"items": items})


class MenuAPIView(APIView):
    def get(self, request):
        menu = [
            {"name": "Cheese Pizza", "description": "Classic pizza with cheese & tomato", "price": 250},
            {"name": "Pasta", "description": "Creamy Alfreddo", "price": 300},
            {"name": "Caesar Salad", "description": "Fresh romaine", "price": 200}
        ]
        return Response(menu)
