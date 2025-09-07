from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Feedback(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:50]

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="menu_images/", blank=True, null=True)

    def __str__(self):
        return self.name

    
class Order(models.Model):
    STATUS_CHOICES = [
        ("PENDING","Pending"),
        ("CONFIRMED", "Confirmed"),
        ("DELIVERED", "Delivered"),
        ("CANCELLED", "Cancelled"),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    items = models.ManyToManyField(Menu, related_name="orders")
    total_amount = models.DecimalField(max_digits = 8, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"


class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)


    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"