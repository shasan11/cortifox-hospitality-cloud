# sales/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Quotation, QuoteItem, Sale, SaleItem, Invoice, InvoiceItem, CustomerPayment, CreditNote, CrnoteItem
from accounting.models import BankAccounts, ChartofAccounts

# Helper function to update ChartofAccounts balance
def update_chart_of_accounts_balance(account, amount):
    account.balance += amount
    account.save()

# Helper function to update BankAccounts balance
def update_bank_account_balance(bank_account, amount):
    bank_account.opening_balance += amount
    bank_account.save()

# Signal for Quotation
@receiver(post_save, sender=Quotation)
def update_on_quotation_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_bank_account_balance(instance.currency, instance.exchange_to_default)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=Quotation)
def update_on_quotation_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_bank_account_balance(instance.currency, -instance.exchange_to_default)

# Signal for QuoteItem
@receiver(post_save, sender=QuoteItem)
def update_on_quote_item_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_chart_of_accounts_balance(instance.product.coa, instance.rate * instance.quantity)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=QuoteItem)
def update_on_quote_item_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_chart_of_accounts_balance(instance.product.coa, -instance.rate * instance.quantity)

# Signal for Sale
@receiver(post_save, sender=Sale)
def update_on_sale_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_bank_account_balance(instance.currency, instance.exchange_to_default)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=Sale)
def update_on_sale_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_bank_account_balance(instance.currency, -instance.exchange_to_default)

# Signal for SaleItem
@receiver(post_save, sender=SaleItem)
def update_on_sale_item_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_chart_of_accounts_balance(instance.product.coa, instance.rate * instance.quantity)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=SaleItem)
def update_on_sale_item_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_chart_of_accounts_balance(instance.product.coa, -instance.rate * instance.quantity)

# Signal for Invoice
@receiver(post_save, sender=Invoice)
def update_on_invoice_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_bank_account_balance(instance.currency, instance.exchange_to_default)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=Invoice)
def update_on_invoice_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_bank_account_balance(instance.currency, -instance.exchange_to_default)

# Signal for InvoiceItem
@receiver(post_save, sender=InvoiceItem)
def update_on_invoice_item_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_chart_of_accounts_balance(instance.product.coa, instance.rate * instance.quantity)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=InvoiceItem)
def update_on_invoice_item_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_chart_of_accounts_balance(instance.product.coa, -instance.rate * instance.quantity)

# Signal for CustomerPayment
@receiver(post_save, sender=CustomerPayment)
def update_on_customer_payment_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_bank_account_balance(instance.bank_acc, -instance.amount)
        update_chart_of_accounts_balance(instance.bank_charge_account, instance.bank_amount)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=CustomerPayment)
def update_on_customer_payment_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_bank_account_balance(instance.bank_acc, instance.amount)
    update_chart_of_accounts_balance(instance.bank_charge_account, -instance.bank_amount)

# Signal for CreditNote
@receiver(post_save, sender=CreditNote)
def update_on_credit_note_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_chart_of_accounts_balance(instance.customer, instance.amount)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=CreditNote)
def update_on_credit_note_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_chart_of_accounts_balance(instance.customer, -instance.amount)

# Signal for CrnoteItem
@receiver(post_save, sender=CrnoteItem)
def update_on_crnote_item_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_chart_of_accounts_balance(instance.product.coa, instance.rate * instance.quantity)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=CrnoteItem)
def update_on_crnote_item_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_chart_of_accounts_balance(instance.product.coa, -instance.rate * instance.quantity)
