from decimal import Decimal
from django.conf import settings
from product.models import Product


class Card(object):
    def __init__(self, request):

        self.session = request.session
        card = self.session.get(settings.CARD_SESSION_ID)

        if not card:
            card = self.session[settings.CARD_SESSION_ID] = {}

        self.card = card

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)

        if product_id not in self.card:
            self.card[product_id] = {"quantity": 0, "price": str(product.PRODPrice)}

        if override_quantity:
            self.card[product_id]["quantity"] = quantity
        else:
            self.card[product_id]["quantity"] += quantity

        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.card:
            del self.card[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.card.keys()
        products = Product.objects.filter(id__in=product_ids)

        card = self.card.copy()
        for product in products:
            card[str(product.id)]["product"] = product

        for item in card.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.card.values())

    def get_total_price(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.card.values()
        )

    def clear(self):
        del self.session[settings.CARD_SESSION_ID]
        self.save()
