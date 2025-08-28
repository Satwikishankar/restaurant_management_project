from django.urls import path
from .views import *

urlpatterns = [
    path("", views.homepage, name="home"),
    path('about/', home, name="about"),
    path('menu/', MenuAPIView.as_view(), name="menu"),
    path('', include('home.urls')),
]