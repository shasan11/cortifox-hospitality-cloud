# Generated by Django 5.0.7 on 2024-07-25 18:50

import core.userSession
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounting', '0002_chartofaccounts_opening_balace'),
        ('branch', '0001_initial'),
        ('contacts', '0001_initial'),
        ('core', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DebitNote',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(editable=False, max_length=20, unique=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('exchange_to_default', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reason', models.TextField()),
                ('note', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('branch', models.ForeignKey(default=core.userSession.get_current_user_branch, on_delete=django.db.models.deletion.PROTECT, related_name='debit_notes', to='branch.branch')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='debit_notes', to='accounting.currency')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='debit_notes_bearing_supplier', to='contacts.contact')),
                ('user_add', models.ForeignKey(default=core.userSession.get_current_user, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='debit_notes', to='core.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='DebitnoteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('tax_type', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('branch', models.ForeignKey(default=core.userSession.get_current_user_branch, on_delete=django.db.models.deletion.PROTECT, related_name='debitnote_items', to='branch.branch')),
                ('debit_note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debitnote_items', to='purchase.debitnote')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='debitnote_items', to='inventory.product')),
                ('user_add', models.ForeignKey(default=core.userSession.get_current_user, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='debitnote_items', to='core.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseBills',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(editable=False, max_length=20, unique=True)),
                ('is_expense', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField()),
                ('exchange_to_default', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit_terms', models.CharField(max_length=100)),
                ('tac', models.TextField(verbose_name='Terms and Conditions')),
                ('note', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('branch', models.ForeignKey(default=core.userSession.get_current_user_branch, on_delete=django.db.models.deletion.PROTECT, related_name='purchase_bills', to='branch.branch')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchase_bills', to='accounting.currency')),
                ('for_supplier_sales', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchase_bills', to='contacts.contact')),
                ('user_add', models.ForeignKey(default=core.userSession.get_current_user, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='purchase_bills', to='core.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseBillsItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('tax_type', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('branch', models.ForeignKey(default=core.userSession.get_current_user_branch, on_delete=django.db.models.deletion.PROTECT, related_name='purchase_bill_items', to='branch.branch')),
                ('coa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='purchase_bill_items', to='accounting.chartofaccounts')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchase_bill_items', to='inventory.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_bill_items', to='purchase.purchasebills')),
                ('user_add', models.ForeignKey(default=core.userSession.get_current_user, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='purchase_bill_items', to='core.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(editable=False, max_length=20, unique=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField()),
                ('exchange_to_default', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit_terms', models.CharField(max_length=100)),
                ('tac', models.TextField(verbose_name='Terms and Conditions')),
                ('note', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('branch', models.ForeignKey(default=core.userSession.get_current_user_branch, on_delete=django.db.models.deletion.PROTECT, related_name='purchase_orders', to='branch.branch')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchase_orders', to='accounting.currency')),
                ('for_supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchase_orders', to='contacts.contact')),
                ('user_add', models.ForeignKey(default=core.userSession.get_current_user, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='purchase_orders', to='core.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('tax', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('branch', models.ForeignKey(default=core.userSession.get_current_user_branch, on_delete=django.db.models.deletion.PROTECT, related_name='purchase_order_items', to='branch.branch')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchase_order_items', to='inventory.product')),
                ('quotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_order_items', to='purchase.purchaseorder')),
                ('user_add', models.ForeignKey(default=core.userSession.get_current_user, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='purchase_order_items', to='core.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierPayment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(editable=False, max_length=20, unique=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('exchange_to_default', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit_terms', models.CharField(max_length=100)),
                ('tac', models.TextField(verbose_name='Terms and Conditions')),
                ('note', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_ref', models.TextField(blank=True, null=True)),
                ('bank_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('revenue_code', models.CharField(choices=[('11111', 'Income Tax relating to an individual or a proprietorship firm'), ('11112', 'TDS on Salary'), ('11113', 'Capital Gain Tax for Individual'), ('11121', 'Income Tax relating to a Government Institutions'), ('11122', 'Income Tax relating to a Public Limited Company'), ('11123', 'Income Tax relating to a Private Limited Company'), ('11124', 'Income Tax relating to Other Entities'), ('11125', 'Capital Gain Tax for Business Entities'), ('11131', 'TDS on Rent'), ('11132', 'TDS on Interest'), ('11133', 'TDS on Dividend or Bonus'), ('11134', 'Income tax on income from other investments'), ('11135', 'Income Tax on Windfall Gain'), ('11139', 'Other Income Tax'), ('11211', 'Social Security Tax calculated at 1% of salary income')], max_length=5)),
                ('tds_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('bank_acc', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='supplier_payments', to='accounting.bankaccounts')),
                ('bank_charge_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='supplier_payments', to='accounting.chartofaccounts')),
                ('branch', models.ForeignKey(default=core.userSession.get_current_user_branch, on_delete=django.db.models.deletion.PROTECT, related_name='supplier_payments', to='branch.branch')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='supplier_payments', to='accounting.currency')),
                ('payment_mode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='supplier_payments', to='accounting.paymentmethod')),
                ('revenue_charge_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='supplier_payments_COA', to='accounting.chartofaccounts')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='supplier_payments', to='contacts.contact')),
                ('user_add', models.ForeignKey(default=core.userSession.get_current_user, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='supplier_payments', to='core.customuser')),
            ],
        ),
    ]
