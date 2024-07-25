from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class ContactGroup(models.Model):
    CUSTOMER = 'customer'
    SUPPLIER = 'supplier'
    TYPE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (SUPPLIER, 'Supplier'),
    ]

    name = models.CharField(max_length=255)
    under = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_groups')
    type = models.CharField(max_length=8, choices=TYPE_CHOICES)
    desc = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='contact_groups_added')

    def __str__(self):
        return self.name


class Contact(models.Model):
    CUSTOMER = 'customer'
    SUPPLIER = 'supplier'
    TYPE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (SUPPLIER, 'Supplier'),
    ]

    contact_type = models.CharField(max_length=8, choices=TYPE_CHOICES)
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    contact_code = models.CharField(max_length=20, unique=True, blank=True)
    pan = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    group = models.ForeignKey(ContactGroup, on_delete=models.CASCADE, related_name='contacts')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='contacts_added')

    def save(self, *args, **kwargs):
        if not self.contact_code:
            self.contact_code = f'C0-{uuid.uuid4().hex[:6].upper()}'
        super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
