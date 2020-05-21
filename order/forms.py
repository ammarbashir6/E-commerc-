from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "FullName",
            "PhoneNumber1",
            "PhoneNumber2",
            "ORDAddressEra",
            "ORDAddress",
        ]
