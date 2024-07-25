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

class PurchaseOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True, editable=False)
    date = models.DateTimeField(default=timezone.now)
    for_supplier = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='purchase_orders')
    expiry_date = models.DateTimeField()
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='purchase_orders')
    exchange_to_default = models.DecimalField(max_digits=10, decimal_places=2)
    credit_terms = models.CharField(max_length=100)
    tac = models.TextField(verbose_name="Terms and Conditions")
    note = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='purchase_orders')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, related_name='purchase_orders')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_unique_code(PurchaseOrder, 'QUOT')
        super(PurchaseOrder, self).save(*args, **kwargs)

    def __str__(self):
        return self.code

class PurchaseOrderItem(models.Model):
    quotation = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='purchase_order_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='purchase_order_items')
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='purchase_order_items')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, related_name='purchase_order_items')

    def __str__(self):
        return f"{self.product} in {self.quotation}"

class PurchaseBills(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True, editable=False)
    is_expense = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    for_supplier_sales = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='purchase_bills')
    expiry_date = models.DateTimeField()
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='purchase_bills')
    exchange_to_default = models.DecimalField(max_digits=10, decimal_places=2)
    credit_terms = models.CharField(max_length=100)
    tac = models.TextField(verbose_name="Terms and Conditions")
    note = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='purchase_bills')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, related_name='purchase_bills')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_unique_code(PurchaseBills, 'PURCHASE')
        super(PurchaseBills, self).save(*args, **kwargs)

    def __str__(self):
        return self.code

class PurchaseBillsItems(models.Model):
    sale = models.ForeignKey(PurchaseBills, on_delete=models.CASCADE, related_name='purchase_bill_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='purchase_bill_items')
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    coa = models.ForeignKey(ChartofAccounts, on_delete=models.PROTECT, null=True, blank=True, related_name='purchase_bill_items')
    tax_type = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='purchase_bill_items')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, related_name='purchase_bill_items')

    def __str__(self):
        return f"{self.product} in {self.sale}"

class SupplierPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True, editable=False)
    date = models.DateTimeField(default=timezone.now)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='supplier_payments')
    exchange_to_default = models.DecimalField(max_digits=10, decimal_places=2)
    credit_terms = models.CharField(max_length=100)
    tac = models.TextField(verbose_name="Terms and Conditions")
    note = models.TextField(blank=True, null=True)
    supplier = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='supplier_payments')
    bank_acc = models.ForeignKey(BankAccounts, on_delete=models.PROTECT, related_name='supplier_payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, null=True, blank=True, related_name='supplier_payments')
    payment_ref = models.TextField(blank=True, null=True)
    bank_charge_account = models.ForeignKey(ChartofAccounts, on_delete=models.PROTECT, null=True, blank=True, related_name='supplier_payments')
    bank_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    revenue_code = models.CharField(max_length=5, choices=REVENUE_CODE_CHOICES)
    revenue_charge_account = models.ForeignKey(ChartofAccounts, on_delete=models.PROTECT, null=True, blank=True, related_name='supplier_payments_COA')
    tds_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='supplier_payments')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, related_name='supplier_payments')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_unique_code(SupplierPayment, 'PAY')
        super(SupplierPayment, self).save(*args, **kwargs)

    def __str__(self):
        return self.code

class DebitNote(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True, editable=False)
    date = models.DateTimeField(default=timezone.now)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='debit_notes')
    exchange_to_default = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='debit_notes_bearing_supplier')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    note = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='debit_notes')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, related_name='debit_notes')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_unique_code(DebitNote, 'CRN')
        super(DebitNote, self).save(*args, **kwargs)

    def __str__(self):
        return self.code

class DebitnoteItem(models.Model):
    debit_note = models.ForeignKey(DebitNote, on_delete=models.CASCADE, related_name='debitnote_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='debitnote_items')
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    tax_type = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, null=True, default=get_current_user, related_name='debitnote_items')
    active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, default=get_current_user_branch, on_delete=models.PROTECT, related_name='debitnote_items')

    def __str__(self):
        return f"{self.product} in {self.debit_note}"
