from django import forms
from .models import Order

# from phonenumber_field.modelfields import PhoneNumberField


class OrderCreateForm(forms.ModelForm):
    # PhoneNumber1 = forms.CharFaild()
    # PhoneNumber2 = PhoneNumberField()

    class Meta:
        model = Order
        fields = [
            "FullName",
            "PhoneNumber1",
            "PhoneNumber2",
            "ORDAddressEra",
            "ORDAddress",
        ]
