from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from .models import TableReservation, Table

@receiver(post_save, sender=TableReservation)
def update_table_status_on_reservation(sender, instance, created, **kwargs):
    if created:
        table = instance.table
        table.status = Table.RESERVED
        table.save()
        instance.active = True
        instance.save()
    else:
        # Check if the reservation time has ended and update status
        if instance.reservation_end < timezone.now():
            instance.active = False
            instance.save()
            table = instance.table
            table.status = Table.AVAILABLE
            table.save()

@receiver(post_delete, sender=TableReservation)
def reset_table_status_on_reservation_cancel(sender, instance, **kwargs):
    table = instance.table
    table.status = Table.AVAILABLE
    table.save()
