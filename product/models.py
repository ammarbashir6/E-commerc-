from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from PIL import Image

# Create your models here.
class Category(models.Model):
    CATName = models.CharField(max_length=200)
    CATARName = models.CharField(max_length=200, verbose_name=("إسم القسم بالعربي"))
    CATNSlug = models.SlugField(
        max_length=200, unique=True, blank=True, verbose_name=("category Slug"),
    )

    def save(self, *args, **kwargs):
        self.CATNSlug = slugify(self.CATName)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ("CATName",)
        verbose_name = "صنف "
        verbose_name_plural = "الاصناف "

    def __str__(self):
        return str(self.CATARName)

    def get_absolute_url(self):
        return reverse("product-list-by-category", args=[self.CATNSlug])


COLOR = (
    ("black", "اسود"),
    ("white", "ابيض"),
    ("red", "احمر"),
    ("blue", "ازرق"),
)


class Product(models.Model):
    PRODCategory = models.ForeignKey(
        "Category", verbose_name=(""), on_delete=models.CASCADE
    )
    PRODName = models.CharField(max_length=200, verbose_name=("إسم المنتج"),)
    PRODARName = models.CharField(
        default="product", max_length=200, verbose_name=(" إسم المنتج عربي"),
    )
    PRODSlug = models.SlugField(
        max_length=200, unique=True, blank=True, verbose_name=("Product Slug"),
    )

    # PRODColor = models.CharField(blank=True, verbose_name=("لون المنتج"), max_length=50)
    PRODDescription = models.TextField(verbose_name=("وصف المنتج"))
    PRODCost = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=("سعر شراء المنتج")
    )

    PRODPrice = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=("سعر بيع المنتج")
    )

    PRODImage = models.ImageField(
        upload_to="Product-images", verbose_name=("صور المنتج")
    )

    PRODAvailabel = models.BooleanField(default=True, verbose_name=("هل المنتج موجود"))
    PRODQuantity = models.IntegerField(verbose_name=("كمية المنتج "))
    PRODCreated = models.DateTimeField(
        auto_now_add=True, verbose_name=("تاريخ إضافة المنتج")
    )
    PRODUpdate = models.DateTimeField(
        auto_now=True, verbose_name=("تاريخ تعديل المنتج")
    )

    def save(self, *args, **kwargs):
        self.PRODSlug = slugify(self.PRODName)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ("PRODName",)
        verbose_name = "المنتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.PRODName

    def get_absolute_url(self):
        return reverse("product-detail", args=[self.PRODSlug])


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    PRODimages = models.ImageField(
        upload_to="product-images", verbose_name="صور المنتج"
    )
    PRODColor = models.CharField(
        verbose_name=("لون المنتج"), choices=COLOR, blank=True, max_length=50
    )

    def __str__(self):
        return str(self.product)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.PRODimages.path)

        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.PRODimages.path)
