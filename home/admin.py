from django.contrib import admin
from .models import Menu, Order

# Register your models here.

admin.site.register(MenuItem)
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "created_at")
    search_fields = ("customer_name",)
    filter_horizontal = ("items",)
