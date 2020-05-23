from django.db import models
from product.models import Product
from django.forms import ModelForm

from phonenumber_field.modelfields import PhoneNumberField

ADDRESSES = (
    ("", "إختار الحي"),
    ("abushrif", "ابو شريف م3"),
    ("square 31", "مربع 31"),
    ("square 32", "مربع 32"),
    ("square 29", "مربع 29"),
    ("square 27", "مربع 27"),
    ("square 26", "مربع 26"),
    ("square 28", "مربع 28"),
    ("square 34", "مربع 34"),
    ("square 42", "مربع 42"),
    ("square 43", "مربع 42"),
    ("alandlos", "الاندلس"),
    ("alnsry", "النصري"),
    ("square 44", "مربع 44"),
    ("square 39", "مربع 39"),
    ("square 46", "مربع 46"),
    ("square 47", "مربع 47"),
    ("alhala ", "الحلة الجديدة"),
    ("alshati", "الشاطئ"),
)


# Create your models here.
class Order(models.Model):
    FullName = models.CharField(max_length=200, verbose_name=("الاسم بالكامل "),)

    # PhoneNumber1 = models.CharField(max_length=10, verbose_name=("رقام الهاتف"))
    # PhoneNumber2 = models.CharField(
    # max_length=10, verbose_name=("رقام هاتف اختياري"), blank=True
    # )
    phoneNumber1 = PhoneNumberField(max_length=10, verbose_name=("رقم الهاتف"))
    PhoneNumber2 = PhoneNumberField(
        max_length=10, blank=True, verbose_name=("رقم هاتف اخر ")
    )
    ORDAddressEra = models.CharField(
        max_length=200, choices=ADDRESSES, verbose_name=(" المنطقة"),
    )
    ORDAddress = models.TextField(verbose_name=(" العنوان بالتفصيل"),)
    ORDACreated = models.DateTimeField(auto_now_add=True, verbose_name=("تاريخ الطلب"),)
    ORDAUpdate = models.DateTimeField(auto_now=True, verbose_name=("تاريخ تعديل الطلب"))
    ORDPaid = models.BooleanField(default=False)

    class Meta:
        ordering = ("-ORDACreated",)
        verbose_name = "طلب المنتج"
        verbose_name_plural = "طلبات المنتجات"

    def __str__(self):
        return f" Order {self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name="items", on_delete=models.CASCADE)
    ORDIProduct = models.ForeignKey(
        Product, verbose_name="order_items", on_delete=models.CASCADE
    )

    ORDIPrice = models.DecimalField(max_digits=10, decimal_places=2)
    ORDIQuantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.ORDIPrice * self.ORDIQuantity
