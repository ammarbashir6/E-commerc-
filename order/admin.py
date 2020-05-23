from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["ORDIProduct"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "FullName",
        "PhoneNumber1",
        "PhoneNumber2",
        "ORDACreated",
        "ORDAUpdate",
        "ORDPaid",
    ]

    list_filter = ["ORDPaid", "ORDACreated", "ORDAUpdate"]

    inlines = [OrderItemInline]
