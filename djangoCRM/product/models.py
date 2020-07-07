from django.db import models

# Create your models here.
#admin login id Puja and password 0123456

class Brand(models.Model):
    name = models.CharField(max_length=100)
    publish = models.BooleanField(default=True)


class Categoria(models.Model):
    name = models.CharField(max_length=200)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Subcategoria(models.Model):
    name = models.CharField(max_length=200)
    publish = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Producto(models.Model):
    name = models.CharField(max_length=200)
    subcategoria = models.ForeignKey(Subcategoria, unique=True, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, blank=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



        

# from django.db import models
from django.conf import settings
from .manager import ProductManager

CURRENCY = settings.CURRENCY


class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    discount_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    final_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    qty = models.PositiveIntegerField(default=0)

    objects = models.Manager()
    broswer = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        self.final_value = self.discount_value if self.discount_value > 0 else self.value
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def tag_final_value(self):
        return f'{self.final_value} {CURRENCY}'
    tag_final_value.short_description = 'Value'
