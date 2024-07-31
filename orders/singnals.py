# signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from sales.models import Sale, SaleItem
from .models import Order, OrderItems

@receiver(post_save, sender=Order)
def create_sale_for_order(sender, instance, created, **kwargs):
    if created:
        Sale.objects.create(
            for_customer_sales=instance.customer,
            date=instance.created,
            expiry_date=instance.expected_delivery_time,
            currency=instance.order_register.branch_of.currency,
            exchange_to_default=1.00,  # Set this as required
            credit_terms="Immediate",  # Set this as required
            tac="Terms and Conditions",  # Set this as required
            note=instance.order_notes,
            user_add=instance.user_add,
            branch=instance.order_register.branch_of,
        )
    else:
        sale = instance.sales_order
        sale.for_customer_sales = instance.customer
        sale.date = instance.created
        sale.expiry_date = instance.expected_delivery_time
        sale.note = instance.order_notes
        sale.user_add = instance.user_add
        sale.branch = instance.order_register.branch_of
        sale.save()

@receiver(post_save, sender=OrderItems)
def create_sale_item_for_order_item(sender, instance, created, **kwargs):
    if created:
        SaleItem.objects.create(
            sale=instance.order.sales_order,
            product=instance.food_item,
            rate=instance.price,
            quantity=instance.qty,
            tax_type="Standard",  # Set this as required
            user_add=instance.user_add,
            branch=instance.order.order_register.branch_of,
        )
    else:
        sale_item = SaleItem.objects.get(id=instance.sales_order_item.id)
        sale_item.product = instance.food_item
        sale_item.rate = instance.price
        sale_item.quantity = instance.qty
        sale_item.tax_type = "Standard"  # Set this as required
        sale_item.user_add = instance.user_add
        sale_item.branch = instance.order.order_register.branch_of
        sale_item.save()

@receiver(post_delete, sender=Order)
def delete_sale_for_order(sender, instance, **kwargs):
    if instance.sales_order:
        instance.sales_order.delete()

@receiver(post_delete, sender=OrderItems)
def delete_sale_item_for_order_item(sender, instance, **kwargs):
    if instance.sales_order_item:
        instance.sales_order_item.delete()
