from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product-list"),
    path(
        "category/<slug:category_slug>/",
        views.product_list,
        name="product-list-by-category",
    ),
    path("product/<slug:slug>/", views.productDetail, name="product-detail"),
    # path("<slug:slug>/", views.product_detail, name="product-detail"),
    # path("<int:id>/slug:product_slug>/", views.product_detail, name="product-detail"),
]
