from django.db import models
from branch.models import Branch
from tables.models import Table
from contacts.models import Contact
from core.models import get_current_user, get_current_user_branch
from inventory.models import Product
from django.contrib.auth.models import User

class OrderRegister(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch_of = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name="Branch", related_name="order_registers", editable=False, default=get_current_user_branch)
    initial_cash = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Initial Cash", editable=False, null=True, blank=True)
    closing_cash = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Closing Cash", editable=False, null=True, blank=True)
    started = models.DateTimeField(auto_now_add=True, verbose_name="Started At")
    ended = models.DateTimeField(auto_now=True, verbose_name="Ended At")
    started_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders_started', null=True, editable=False)
    ended_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders_ended', null=True, editable=False)
    status = models.CharField(max_length=10, choices=[("O", "Open"), ("C", "Closed")], default="O", verbose_name="Status")

    def __str__(self):
        return f"Register {self.id} - {self.branch_of}"

order_choices = (
    ("P", "Pending"),
    ("C", "Confirmed"),
    ("IP", "In Progress"),
    ("R", "Ready"),
    ("D", "Delivered"),
    ("CC", "Cancelled")
)

main_choices = (
    ("D", "Dine In Orders"),
    ("T", "Take Away Orders"),
    ("Dl", "Delivery Orders"),
    ("O", "Online Order"),
)

class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_register = models.ForeignKey(OrderRegister, on_delete=models.PROTECT, related_name='orders')
    customer = models.ForeignKey(Contact, on_delete=models.PROTECT, verbose_name="Customer", blank=True, null=True, related_name='orders')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name="Table", blank=True, null=True, related_name="orders_at_table")
    delivery_address = models.TextField(verbose_name="Delivery Address", blank=True, null=True)
    contact_number = models.CharField(max_length=15, verbose_name="Contact Number", blank=True, null=True)
    expected_delivery_time = models.DateTimeField(verbose_name="Expected Delivery Time", blank=True, null=True)
    order_type = models.CharField(max_length=2, choices=main_choices, verbose_name="Order Type", default="D")
    user_add = models.ForeignKey(Contact, on_delete=models.PROTECT, verbose_name="Order Opened By", editable=False, null=True, default=get_current_user, related_name='opened_orders')
    completion_status = models.BooleanField(default=False, verbose_name="Completed")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Amount", editable=False, null=True, blank=True)
    order_notes = models.TextField(verbose_name="Order Notes", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Time Created")
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.table:
            tbl = Table.objects.get(id=self.table.pk)
            tbl.status = "Reserved"
            tbl.save()
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} - {self.order_type}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

class OrderItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Order", related_name='order_items')
    food_item = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Item", related_name='order_items')
    qty = models.PositiveSmallIntegerField(verbose_name="Quantity")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Discount", default=0.00)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Sub Total", editable=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total", editable=False, null=True, blank=True)
    description = models.TextField("Description", blank=True, null=True)
    timestamp = models.DateTimeField(verbose_name="Time Stamp", auto_now_add=True)
    status = models.CharField(max_length=2, choices=order_choices, verbose_name="Order Choices", default="P")
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Order taken by", editable=False, null=True, default=get_current_user, related_name='order_items_taken')
    active = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.sub_total = self.price * self.qty
        self.total = self.sub_total - self.discount
        super(OrderItems, self).save(*args, **kwargs)

    def __str__(self):
        return f"OrderItem {self.id} - {self.food_item}"

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
