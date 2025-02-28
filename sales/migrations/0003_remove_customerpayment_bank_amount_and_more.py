# Generated by Django 5.0.7 on 2024-07-30 22:17

import core.userSession
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0001_initial'),
        ('contacts', '0001_initial'),
        ('core', '0001_initial'),
        ('sales', '0002_invoice_is_cleared'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerpayment',
            name='bank_amount',
        ),
        migrations.RemoveField(
            model_name='customerpayment',
            name='bank_charge_account',
        ),
        migrations.RemoveField(
            model_name='customerpayment',
            name='from_customer',
        ),
        migrations.RemoveField(
            model_name='customerpayment',
            name='payment_ref',
        ),
        migrations.RemoveField(
            model_name='customerpayment',
            name='revenue_charge_account',
        ),
        migrations.RemoveField(
            model_name='customerpayment',
            name='tds_amount',
        ),
        migrations.AddField(
            model_name='customerpayment',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customer_payments', to='contacts.contact'),
        ),
        migrations.AddField(
            model_name='customerpayment',
            name='invoices',
            field=models.ManyToManyField(related_name='invoices_customer_payment', to='sales.invoice'),
        ),
        migrations.AddField(
            model_name='customerpayment',
            name='payment_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customerpayment',
            name='sales',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sale_order_to_customer_payment', to='sales.sale'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='sales',
            field=models.ManyToManyField(related_name='sales_order_to_invoice', to='sales.sale'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='sales',
            field=models.ManyToManyField(related_name='invoice_render_to_customer_payment', to='sales.sale'),
        ),
        migrations.AlterField(
            model_name='customerpayment',
            name='branch',
            field=models.ForeignKey(default=core.userSession.get_current_user_branch, on_delete=django.db.models.deletion.PROTECT, related_name='customer_payments', to='branch.branch'),
        ),
        migrations.AlterField(
            model_name='customerpayment',
            name='revenue_code',
            field=models.CharField(blank=True, choices=[('11111', 'Income Tax relating to an individual or a proprietorship firm'), ('11112', 'TDS on Salary'), ('11113', 'Capital Gain Tax for Individual'), ('11121', 'Income Tax relating to a Government Institutions'), ('11122', 'Income Tax relating to a Public Limited Company'), ('11123', 'Income Tax relating to a Private Limited Company'), ('11124', 'Income Tax relating to Other Entities'), ('11125', 'Capital Gain Tax for Business Entities'), ('11131', 'TDS on Rent'), ('11132', 'TDS on Interest'), ('11133', 'TDS on Dividend or Bonus'), ('11134', 'Income tax on income from other investments'), ('11135', 'Income Tax on Windfall Gain'), ('11139', 'Other Income Tax'), ('11211', 'Social Security Tax calculated at 1% of salary income')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customerpayment',
            name='user_add',
            field=models.ForeignKey(default=core.userSession.get_current_user, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='customer_payments', to='core.customuser'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='user_add',
            field=models.ForeignKey(default=core.userSession.get_current_user, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='invoices', to='core.customuser'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='user_add',
            field=models.ForeignKey(default=core.userSession.get_current_user, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='invoice_items', to='core.customuser'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='branch',
            field=models.ForeignKey(default=core.userSession.get_current_user_branch, on_delete=django.db.models.deletion.PROTECT, related_name='quotations', to='branch.branch'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='user_add',
            field=models.ForeignKey(default=core.userSession.get_current_user, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='quotations', to='core.customuser'),
        ),
        migrations.AlterField(
            model_name='quoteitem',
            name='user_add',
            field=models.ForeignKey(default=core.userSession.get_current_user, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='quote_items', to='core.customuser'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='user_add',
            field=models.ForeignKey(default=core.userSession.get_current_user, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='sales', to='core.customuser'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='user_add',
            field=models.ForeignKey(default=core.userSession.get_current_user, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='sale_items', to='core.customuser'),
        ),
    ]
