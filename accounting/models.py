from django.db import models
from core.userSession import get_current_user
from django.contrib.auth.models import User
from contacts.models import Contact
import uuid

class ChartofAccounts(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ("Assets", 'Assets'),
        ("Liability", 'Liability'),
        ("Equity", 'Equity'),
        ("Income", 'Income'),
        ("Expenses", 'Expenses'),
    ]
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    under = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_accounts')
    coa_type=models.CharField(max_length=100,choices=ACCOUNT_TYPE_CHOICES,default="Assets")
    desc = models.TextField(blank=True, null=True)
    opening_balance=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    code = models.CharField(max_length=20, unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    user_add=models.ForeignKey(User,on_delete=models.PROTECT,editable=False,null=True,default=get_current_user)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Chart of Accounts"
        verbose_name_plural = "Chart of Accounts"

class BankAccounts(models.Model):
    acc_type=[
        ("Cash","Cash"),
        ("Bank","Bank")
    ]
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    acc_type=models.CharField(max_length=100,choices=acc_type,default="Bank",verbose_name="Bank/Cash")
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255,blank=True,null=True,verbose_name="Bank Name")
    code = models.CharField(max_length=20, unique=True,blank=True,null=True)
    type = models.CharField(max_length=20, choices=[('savings', 'Savings'), ('current', 'Current')],blank=True,null=True)
    account_number = models.CharField(max_length=50,blank=True,null=True)
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE, blank=True, null=True, related_name='bank_accounts')
    opening_balance=models.DecimalField(max_digits=10,decimal_places=2)    
    description = models.TextField(blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated=models.DateTimeField(auto_now=True,blank=True,null=True)
    user_add=models.ForeignKey(User,on_delete=models.PROTECT,editable=False,null=True,default=get_current_user)
    active=models.BooleanField(default=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bank Accounts"
        verbose_name_plural = "Bank Accounts"

class Currency(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100,verbose_name="Currency Name")
    symbol=models.CharField(max_length=10,verbose_name="Symbol")
    decimal_places=models.PositiveBigIntegerField(verbose_name="Decimal Places",default=2)
    is_default=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    user_add=models.ForeignKey(User,on_delete=models.PROTECT,editable=False,null=True,default=get_current_user)
    active=models.BooleanField(default=True)


    class Meta:
        verbose_name_plural="Currency"


    def __str__(self):
        return self.name   

class PaymentMethod(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField(blank=True, null=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2)   
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    user_add=models.ForeignKey(User,on_delete=models.PROTECT,editable=False,null=True,default=get_current_user)
    active=models.BooleanField(default=True)
 
 

def generate_custom_journal():
    last_shipment = JournalEntryItems.objects.all().order_by('-id').first()
    last_shipment_id = last_shipment.id if last_shipment else 0
    unique_number = last_shipment_id + 500

    return f"JRNL-{unique_number:08d}" 
 
class JournalEntry(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    jounral_entry_no=models.CharField(blank=True,null=True,default=generate_custom_journal,max_length=65)
    bill_no = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    reference = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    user_add=models.ForeignKey(User,on_delete=models.PROTECT,editable=False,null=True,default=get_current_user)
    active=models.BooleanField(default=True)


    def __str__(self):
        return f"Journal Entry {self.bill_no}"

    class Meta:
        verbose_name = "Journal Entry"
        verbose_name_plural = "Journal Entries" 
        
class JournalEntryItems(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)    
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name='items')
    chart_of_accounts = models.ForeignKey(ChartofAccounts, on_delete=models.CASCADE, related_name='journal_entries')
    dr_amount = models.DecimalField(max_digits=10, decimal_places=2)
    cr_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    user_add=models.ForeignKey(User,on_delete=models.PROTECT,editable=False,null=True,default=get_current_user)
    active=models.BooleanField(default=True)


    def __str__(self):
        return f"Journal Entry Items {self.id} for {self.journal_entry}"

    class Meta:
        verbose_name = "Journal Entry Items"
        verbose_name_plural = "Journal Entry Items"
        
        
class CashTransfers(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    bill_no = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    paid_from = models.ForeignKey(BankAccounts, related_name='transfers_paid_from', on_delete=models.CASCADE)
    to_account = models.ForeignKey(BankAccounts, related_name='transfers_to_account', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    exchange_rate=models.FloatField(default=1)
    reference = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    user_add=models.ForeignKey(User,on_delete=models.PROTECT,editable=False,null=True,default=get_current_user)
    active=models.BooleanField(default=True)


    def __str__(self):
        return f"Cash Transfer {self.bill_no}"

    class Meta:
        verbose_name = "Cash Transfer"
        verbose_name_plural = "Cash Transfers"
              

class ChequeRegister(models.Model):
    CONTACT_CHOICES = [
        ('recieved', 'Cheque Recieved'),
        ('issued', 'Cheque Issued'),
    ]

    STATUS_CHOICES = [
        ('cleared', 'Cleared'),
        ('pending', 'Pending'),
        ('partial', 'Partial'),
        ('bounced', 'Bounced'),
    ]

    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    bank_account = models.ForeignKey('BankAccounts', on_delete=models.CASCADE, related_name='cheques')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    payee_name = models.CharField(max_length=255)
    cheque_no = models.CharField(max_length=50)
    issued_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    cheque_type = models.CharField(max_length=10, choices=CONTACT_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Cheque {self.cheque_no} ({self.payee_name})"

    class Meta:
        verbose_name = "Cheque Register"
        verbose_name_plural = "Cheque Register"       
