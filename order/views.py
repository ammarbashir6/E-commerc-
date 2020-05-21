from django.shortcuts import render
from card.card import Card
from .forms import OrderCreateForm
from .models import OrderItem

# Create your views here.
def order_create(request):
    card = Card(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in card:
                OrderItem.objects.create(
                    order=order,
                    ORDIProduct=item["product"],
                    ORDIPrice=item["price"],
                    ORDIQuantity=item["quantity"],
                )
            card.clear()
            return render(request, "order/created_order.html", {"order": order},)
    else:
        form = OrderCreateForm()
    return render(request, "order/create_order.html", {"card": card, "form": form})
