from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class Floor(models.Model):
    sno = models.IntegerField()
    floorname = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='floors_added')

    def __str__(self):
        return self.floorname


class Table(models.Model):
    AVAILABLE = 'available'
    RESERVED = 'reserved'
    PENDING = 'pending'
    NOT_AVAILABLE = 'not available'
    MAINTENANCE = 'maintenance'
    STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (RESERVED, 'Reserved'),
        (PENDING, 'Pending'),
        (NOT_AVAILABLE, 'Not Available'),
        (MAINTENANCE, 'Maintenance')
    ]

    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='tables')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20, unique=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=AVAILABLE)
    seating_capacity = models.IntegerField()
    table_charge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tables_added')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = f'T-{uuid.uuid4().hex[:6].upper()}'
        super(Table, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class TableReservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reservations')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations_as_customer')  # Assuming User as Customer
    reservation_start = models.DateTimeField()
    reservation_end = models.DateTimeField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reservations_added')

    def __str__(self):
        return f'Reservation for {self.table.name} by {self.customer.username}'
