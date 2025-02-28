# Generated by Django 5.0.7 on 2024-07-25 05:06

import core.userSession
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0001_initial'),
        ('contacts', '0001_initial'),
        ('inventory', '0001_initial'),
        ('tables', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('delivery_address', models.TextField(blank=True, null=True, verbose_name='Delivery Address')),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Contact Number')),
                ('expected_delivery_time', models.DateTimeField(blank=True, null=True, verbose_name='Expected Delivery Time')),
                ('order_type', models.CharField(choices=[('D', 'Dine In Orders'), ('T', 'Take Away Orders'), ('Dl', 'Delivery Orders'), ('O', 'Online Order')], default='D', max_length=2, verbose_name='Order Type')),
                ('completion_status', models.BooleanField(default=False, verbose_name='Completed')),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Total Amount')),
                ('order_notes', models.TextField(blank=True, null=True, verbose_name='Order Notes')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Time Created')),
                ('active', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='contacts.contact', verbose_name='Customer')),
                ('table', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders_at_table', to='tables.table', verbose_name='Table')),
                ('user_add', models.ForeignKey(default=core.userSession.get_current_user, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='opened_orders', to='contacts.contact', verbose_name='Order Opened By')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('qty', models.PositiveSmallIntegerField(verbose_name='Quantity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Discount')),
                ('sub_total', models.DecimalField(decimal_places=2, editable=False, max_digits=10, verbose_name='Sub Total')),
                ('total', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Total')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Time Stamp')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('C', 'Confirmed'), ('IP', 'In Progress'), ('R', 'Ready'), ('D', 'Delivered'), ('CC', 'Cancelled')], default='P', max_length=2, verbose_name='Order Choices')),
                ('active', models.BooleanField(default=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_items', to='inventory.product', verbose_name='Item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.order', verbose_name='Order')),
                ('user_add', models.ForeignKey(default=core.userSession.get_current_user, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='order_items_taken', to=settings.AUTH_USER_MODEL, verbose_name='Order taken by')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Order Items',
            },
        ),
        migrations.CreateModel(
            name='OrderRegister',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('initial_cash', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Initial Cash')),
                ('closing_cash', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Closing Cash')),
                ('started', models.DateTimeField(auto_now_add=True, verbose_name='Started At')),
                ('ended', models.DateTimeField(auto_now=True, verbose_name='Ended At')),
                ('status', models.CharField(choices=[('O', 'Open'), ('C', 'Closed')], default='O', max_length=10, verbose_name='Status')),
                ('branch_of', models.ForeignKey(default=core.userSession.get_current_user_branch, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='order_registers', to='branch.branch', verbose_name='Branch')),
                ('ended_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_ended', to=settings.AUTH_USER_MODEL)),
                ('started_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_started', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_register',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='orders.orderregister'),
        ),
    ]
