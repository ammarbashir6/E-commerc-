from django.contrib import admin
from .models import Category, Product, ProductImages

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["CATARName", "CATNSlug"]

    # prepopuulated_fields = {"CATNSlug": ("CATName",)}


class ImageProductInline(admin.TabularInline):
    model = ProductImages
    raw_id_fields = ["product"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "PRODARName",
        "PRODSlug",
        "PRODPrice",
        "PRODCost",
        "PRODAvailabel",
        "PRODCreated",
        "PRODUpdate",
    ]

    list_fliter = ["PRODAvailabel", "PRODCreated", "PRODUpdate"]

    list_editabel = ["PRODPrice", "PRODAvailabel"]

    inlines = [ImageProductInline]
    # prepopuulated_fields = {"slug": ("PRODName")}
