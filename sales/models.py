from django.db import models
from django.utils import timezone
from inventory.models import Product
from contacts.models import Contact
from accounting.models import Currency, BankAccounts, PaymentMethod, ChartofAccounts
from core.models import CustomUser as User
from branch.models import Branch
from core.userSession import get_current_user
from core.userSession import get_current_user_branch

REVENUE_CODE_CHOICES = [
    ('11111', 'Income Tax relating to an individual or a proprietorship firm'),
    ('11112', 'TDS on Salary'),
    ('11113', 'Capital Gain Tax for Individual'),
    ('11121', 'Income Tax relating to a Government Institutions'),
    ('11122', 'Income Tax relating to a Public Limited Company'),
    ('11123', 'Income Tax relating to a Private Limited Company'),
    ('11124', 'Income Tax relating to Other Entities'),
    ('11125', 'Capital Gain Tax for Business Entities'),
    ('11131', 'TDS on Rent'),
    ('11132', 'TDS on Interest'),
    ('11133', 'TDS on Dividend or Bonus'),
    ('11134', 'Income tax on income from other investments'),
    ('11135', 'Income Tax on Windfall Gain'),
    ('11139', 'Other Income Tax'),
    ('11211', 'Social Security Tax calculated at 1% of salary income'),
]

def generate_unique_code(model, prefix):
    last_record = model.objects.all().order_by('id').last()
    if not last_record:
        return f"{prefix}1001"
    last_code = last_record.code
    last_number = int(last_code[len(prefix):])
    new_number = last_number + 1
    return f"{prefix}{new_number:04d}"

class Quotation(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True, editable=False)
    date = models.DateTimeField(default=timezone.now)
    for_customer = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='quotations')
    expiry_date = models.DateTimeField()
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='quotations')
    exchange_to_default = models.DecimalField(max_digits=10, decimal_places=2)
    credit_terms = models.CharField(max_length=100)
    tac = models.TextField(verbose_name="Terms and Conditions")
    note = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='quotations')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, null=True, blank=True, related_name='quotations')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_unique_code(Quotation, 'QUOT')
        super(Quotation, self).save(*args, **kwargs)

    def __str__(self):
        return self.code

class QuoteItem(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name='quote_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='quote_items')
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='quote_items')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, related_name='quote_items')

    def __str__(self):
        return f"{self.product} in {self.quotation}"

class Sale(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True, editable=False)
    date = models.DateTimeField(default=timezone.now)
    for_customer_sales = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='sales_customer')
    expiry_date = models.DateTimeField()
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='sales')
    exchange_to_default = models.DecimalField(max_digits=10, decimal_places=2)
    credit_terms = models.CharField(max_length=100)
    tac = models.TextField(verbose_name="Terms and Conditions")
    note = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='sales')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, related_name='sales')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_unique_code(Sale, 'SALE')
        super(Sale, self).save(*args, **kwargs)

    def __str__(self):
        return self.code

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='sale_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='sale_items')
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    tax_type = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='sale_items')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, related_name='sale_items')

    def __str__(self):
        return f"{self.product} in {self.sale}"

class Invoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True, editable=False)
    date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField()
    for_customer_invoice = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='invoices')
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='invoices')
    exchange_to_default = models.DecimalField(max_digits=10, decimal_places=2)
    credit_terms = models.CharField(max_length=100)
    tac = models.TextField(verbose_name="Terms and Conditions")
    note = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='invoices')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, related_name='invoices')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_unique_code(Invoice, 'INV')
        super(Invoice, self).save(*args, **kwargs)

    def __str__(self):
        return self.code

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='invoice_items')
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    tax_type = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='invoice_items')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, related_name='invoice_items')

    def __str__(self):
        return f"{self.product} in {self.invoice}"

class CustomerPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True, editable=False)
    date = models.DateTimeField(default=timezone.now)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='customer_payments')
    exchange_to_default = models.DecimalField(max_digits=10, decimal_places=2)
    credit_terms = models.CharField(max_length=100)
    tac = models.TextField(verbose_name="Terms and Conditions")
    note = models.TextField(blank=True, null=True)
    from_customer = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='customer_payments_form_acc')
    bank_acc = models.ForeignKey(BankAccounts, on_delete=models.PROTECT, related_name='customer_payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, null=True, blank=True, related_name='customer_payments')
    payment_ref = models.TextField(blank=True, null=True)
    bank_charge_account = models.ForeignKey(ChartofAccounts, on_delete=models.PROTECT, null=True, blank=True, related_name='customer_payments_bank_Charge_store')
    bank_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    revenue_code = models.CharField(max_length=5, choices=REVENUE_CODE_CHOICES, blank=True, null=True,)
    revenue_charge_account = models.ForeignKey(ChartofAccounts, on_delete=models.PROTECT, null=True, blank=True, related_name='customer_payments')
    tds_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='customer_payments_user_add')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, related_name='customer_payments_default_branch')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_unique_code(CustomerPayment, 'PAY')
        super(CustomerPayment, self).save(*args, **kwargs)

    def __str__(self):
        return self.code

class CreditNote(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True, editable=False)
    date = models.DateTimeField(default=timezone.now)
    for_customer_credit = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='credit_notes_bearing_customer')
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='credit_notes')
    exchange_to_default = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='credit_notes')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    note = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='credit_notes')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, related_name='credit_notes')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_unique_code(CreditNote, 'CRN')
        super(CreditNote, self).save(*args, **kwargs)

    def __str__(self):
        return self.code

class CrnoteItem(models.Model):
    credit_note = models.ForeignKey(CreditNote, on_delete=models.CASCADE, related_name='crnote_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='crnote_items')
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    tax_type = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='crnote_items_user_add')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, related_name='crnote_items_branch_main')

    def __str__(self):
        return f"{self.product} in {self.credit_note}"
