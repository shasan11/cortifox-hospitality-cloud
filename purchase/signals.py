# purchase/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PurchaseOrder, PurchaseOrderItem, PurchaseBills, PurchaseBillsItems, SupplierPayment, DebitNote, DebitnoteItem
from accounting.models import BankAccounts, ChartofAccounts

# Helper function to update ChartofAccounts balance
def update_chart_of_accounts_balance(account, amount):
    account.balance += amount
    account.save()

# Helper function to update BankAccounts balance
def update_bank_account_balance(bank_account, amount):
    bank_account.opening_balance += amount
    bank_account.save()

# Signal for PurchaseOrder
@receiver(post_save, sender=PurchaseOrder)
def update_on_purchase_order_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_bank_account_balance(instance.currency, instance.exchange_to_default)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=PurchaseOrder)
def update_on_purchase_order_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_bank_account_balance(instance.currency, -instance.exchange_to_default)

# Signal for PurchaseOrderItem
@receiver(post_save, sender=PurchaseOrderItem)
def update_on_purchase_order_item_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_chart_of_accounts_balance(instance.product.coa, instance.rate * instance.quantity)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=PurchaseOrderItem)
def update_on_purchase_order_item_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_chart_of_accounts_balance(instance.product.coa, -instance.rate * instance.quantity)

# Signal for PurchaseBills
@receiver(post_save, sender=PurchaseBills)
def update_on_purchase_bills_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_bank_account_balance(instance.currency, instance.exchange_to_default)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=PurchaseBills)
def update_on_purchase_bills_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_bank_account_balance(instance.currency, -instance.exchange_to_default)

# Signal for PurchaseBillsItems
@receiver(post_save, sender=PurchaseBillsItems)
def update_on_purchase_bills_items_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_chart_of_accounts_balance(instance.coa, instance.rate * instance.quantity)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=PurchaseBillsItems)
def update_on_purchase_bills_items_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_chart_of_accounts_balance(instance.coa, -instance.rate * instance.quantity)

# Signal for SupplierPayment
@receiver(post_save, sender=SupplierPayment)
def update_on_supplier_payment_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_bank_account_balance(instance.bank_acc, -instance.amount)
        update_chart_of_accounts_balance(instance.bank_charge_account, instance.bank_amount)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=SupplierPayment)
def update_on_supplier_payment_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_bank_account_balance(instance.bank_acc, instance.amount)
    update_chart_of_accounts_balance(instance.bank_charge_account, -instance.bank_amount)

# Signal for DebitNote
@receiver(post_save, sender=DebitNote)
def update_on_debit_note_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_chart_of_accounts_balance(instance.customer, instance.amount)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=DebitNote)
def update_on_debit_note_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_chart_of_accounts_balance(instance.customer, -instance.amount)

# Signal for DebitnoteItem
@receiver(post_save, sender=DebitnoteItem)
def update_on_debit_note_item_save(sender, instance, created, **kwargs):
    if created:
        # Add logic to update BankAccounts and ChartofAccounts on creation
        update_chart_of_accounts_balance(instance.product.coa, instance.rate * instance.quantity)
    else:
        # Add logic to update BankAccounts and ChartofAccounts on update
        pass

@receiver(post_delete, sender=DebitnoteItem)
def update_on_debit_note_item_delete(sender, instance, **kwargs):
    # Add logic to update BankAccounts and ChartofAccounts on deletion
    update_chart_of_accounts_balance(instance.product.coa, -instance.rate * instance.quantity)
