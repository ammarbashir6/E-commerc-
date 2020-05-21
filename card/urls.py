from django.urls import path
from . import views

urlpatterns = [
    path("", views.cardDetail, name="card-detail"),
    path("add/<int:product_id>", views.addCard, name="add-card"),
    path("remove/<int:product_id>", views.removeCard, name="remove-card"),
]
