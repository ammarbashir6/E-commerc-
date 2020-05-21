from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .card import Card
from .forms import CardAddProductForm

from product.models import Product

# Create your views here.
@require_POST
def addCard(request, product_id):
    card = Card(request)
    product = get_object_or_404(Product, id=product_id)
    form = CardAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        card.add(product, cd["quantity"], cd["override"])
    return redirect("card-detail")


@require_POST
def removeCard(request, product_id):
    card = Card(request)
    product = get_object_or_404(Product, id=product_id)
    card.remove(product)
    return redirect("card-detail")


def cardDetail(request):
    card = Card(request)

    for item in card:
        item["update_quantity_form"] = CardAddProductForm(
            initial={"quantity": item["quantity"], "override": True}
        )
    return render(request, "card/card_detail.html", {"card": card})
