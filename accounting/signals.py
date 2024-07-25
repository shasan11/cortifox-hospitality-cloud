from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db import transaction
from .models import CashTransfers, JournalEntry, ChequeRegister, BankAccounts, Currency
from decimal import Decimal

# Signal for generating auto-incremented bill number for CashTransfers
@receiver(pre_save, sender=CashTransfers)
def generate_cash_transfer_bill_no(sender, instance, **kwargs):
    if not instance.bill_no:
        last_bill_no = CashTransfers.objects.order_by('id').last()
        new_id = (last_bill_no.id + 1) if last_bill_no else 1
        instance.bill_no = f"CT-{new_id}"

# Signal for generating auto-incremented bill number for JournalEntry
@receiver(pre_save, sender=JournalEntry)
def generate_journal_entry_bill_no(sender, instance, **kwargs):
    if not instance.bill_no:
        last_bill_no = JournalEntry.objects.order_by('id').last()
        new_id = (last_bill_no.id + 1) if last_bill_no else 1
        instance.bill_no = f"JE-{new_id}"

# Signal for updating balance in BankAccounts after ChequeRegister is updated to 'cleared'
@receiver(post_save, sender=ChequeRegister)
def update_bank_account_balance(sender, instance, **kwargs):
    if instance.status == 'cleared':
        account = instance.bank_account
        if instance.cheque_type == 'issued':
            account.opening_balance = Decimal(account.opening_balance) - Decimal(instance.amount)
        elif instance.cheque_type == 'recieved':
            account.opening_balance = Decimal(account.opening_balance) + Decimal(instance.amount)
        account.save()

# Signal for validating currency before performing a cash transfer
@receiver(pre_save, sender=CashTransfers)
def validate_cash_transfer_currency(sender, instance, **kwargs):
    if instance.paid_from and instance.to_account:
        if instance.paid_from.currency_id != instance.to_account.currency_id:
            raise ValueError("Cannot perform cash transfer between different currencies.")

# Signal for handling default currency management
@receiver(pre_save, sender=Currency)
def handle_default_currency(sender, instance, **kwargs):
    if instance.is_default:
        with transaction.atomic():
            Currency.objects.filter(is_default=True).exclude(pk=instance.pk).update(is_default=False)

# Signal to handle the bank balance after the cash transfer
@receiver(post_save, sender=CashTransfers)
def update_bank_account_balances_from_cash_transfer(sender, instance, **kwargs):
    if instance.paid_from and instance.to_account:
        # Deduct amount from paid_from account
        paid_from_account = instance.paid_from
        paid_from_account.opening_balance -= instance.amount
        paid_from_account.save()

        # Add amount to to_account
        to_account = instance.to_account
        to_account.opening_balance += instance.amount
        to_account.save()

# Signal to validate the minimum balance in the account before issuing a cheque
@receiver(pre_save, sender=ChequeRegister)
def validate_cheque_issuance_balance(sender, instance, **kwargs):
    if instance.cheque_type == 'issued' and instance.bank_account:
        if instance.bank_account.opening_balance < instance.amount:
            raise ValueError("Insufficient balance to issue the cheque.")
