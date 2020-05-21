from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, ProductImages
from card.card import Card
from card.forms import CardAddProductForm

# Create your views here.


def product_list(request, category_slug=None):
    category = None

    categories = Category.objects.all()
    products = Product.objects.filter(PRODAvailabel=True)
    # prodimages = ProductImage.objects.all()

    if category_slug:
        category = get_object_or_404(Category, CATNSlug=category_slug)
        products = Product.objects.filter(PRODCategory=category)
    return render(
        request,
        "product/product_list.html",
        {"category": category, "categories": categories, "products": products,},
    )


####################### Product Detail ####################################


def productDetail(request, slug):
    product = get_object_or_404(Product, PRODSlug=slug)
    productImages = ProductImages.objects.all().filter(product=product)
    # categories = Category.objects.all().filter(product=product)
    card_product_form = CardAddProductForm()

    return render(
        request,
        "product/product_detail.html",
        {
            "product": product,
            "productImages": productImages,
            # "categories": categories,
            "card_product_form": card_product_form,
            "title": "product.PRODARName",
        },
    )
