from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    under = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_categories')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='categories_added')

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    short_name = models.CharField(max_length=50)
    accept_fraction = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='units_added')

    def __str__(self):
        return self.name


class VariantAttribute(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='variant_attributes_added')

    def __str__(self):
        return self.name


class VariantAttributeItem(models.Model):
    name = models.CharField(max_length=255)
    variant_attribute = models.ForeignKey(VariantAttribute, on_delete=models.CASCADE, related_name='items')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='variant_attribute_items_added')

    def __str__(self):
        return self.name


class Product(models.Model):
    SERVICE = 'service'
    TYPE = 'product'
    TYPE_CHOICES = [
        (SERVICE, 'Service'),
        (TYPE, 'Product')
    ]

    VAT_13 = '13% vat'
    VAT_0 = '0 vat'
    NO_VAT = 'no vat'
    TAX_TYPE_CHOICES = [
        (VAT_13, '13% VAT'),
        (VAT_0, '0 VAT'),
        (NO_VAT, 'No VAT')
    ]

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    tax_type = models.CharField(max_length=10, choices=TAX_TYPE_CHOICES)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_service_charge = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, related_name='products')
    desc = models.TextField(blank=True, null=True)
    variant_attribute_items = models.ManyToManyField(VariantAttributeItem, related_name='products')
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='products_added')

    def __str__(self):
        return self.name
