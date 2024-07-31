from sales.models import Sale, SaleItem, Invoice, InvoiceItem, CustomerPayment, PaymentMethod
from sales.models import generate_unique_code
from django.utils import timezone

def create_invoice_from_sale(sale_id):
    try:
        sale = Sale.objects.get(id=sale_id)
        
        invoice = Invoice.objects.create(
            code=generate_unique_code(Invoice, 'INV'),
            date=timezone.now(),
            expiry_date=sale.expiry_date,
            for_customer_invoice=sale.for_customer_sales,
            currency=sale.currency,
            exchange_to_default=sale.exchange_to_default,
            credit_terms=sale.credit_terms,
            tac=sale.tac,
            note=sale.note,
            user_add=sale.user_add,
            branch=sale.branch,
        )
        
        for sale_item in sale.sale_items.all():
            invoice_item = InvoiceItem.objects.create(
                invoice=invoice,
                product=sale_item.product,
                rate=sale_item.rate,
                quantity=sale_item.quantity,
                tax_type=sale_item.tax_type,
                user_add=sale_item.user_add,
                branch=sale_item.branch,
            )
            invoice_item.sales.add(sale)
        
        invoice.sales.add(sale)
        return invoice
    except Sale.DoesNotExist:
        print(f"Sale with id {sale_id} does not exist")
        return None

def create_customer_payments(sale_id, invoice_id, payments):
    try:
        sale = Sale.objects.get(id=sale_id)
        invoice = Invoice.objects.get(id=invoice_id)
        
        for paymentmethod_id, amount in payments.items():
            payment_method = PaymentMethod.objects.get(id=paymentmethod_id)
            
            customer_payment = CustomerPayment.objects.create(
                date=timezone.now(),
                amount=amount,
                paymentmethod=payment_method,
                for_customer_payment=sale.for_customer_sales,
                invoice=invoice,
                customer=sale.customer,
                currency=sale.currency,
                exchange_to_default=sale.exchange_to_default,
                user_add=sale.user_add,
                branch=sale.branch,
            )
            
            customer_payment.sales.add(sale)
            customer_payment.invoices.add(invoice)
        
        return True
    except Sale.DoesNotExist:
        print(f"Sale with id {sale_id} does not exist")
        return False
    except Invoice.DoesNotExist:
        print(f"Invoice with id {invoice_id} does not exist")
        return False
    except PaymentMethod.DoesNotExist:
        print(f"PaymentMethod with id {paymentmethod_id} does not exist")
        return False

def Checkout(sales_id, payments, payment_type):
    try:
        sales = Sale.objects.get(id=sales_id)
        
        if payment_type == "Complementary":
            sales.note = f"{sales.id} is a Complementary order"
            sales.save()
        
        elif payment_type == "Pay Later":
            create_invoice_from_sale(sales.id)
        
        elif payment_type == "Split Payment":
            invoice = create_invoice_from_sale(sales.id)
            if invoice:
                create_customer_payments(sales.id, invoice.id, payments)
        
        return True
    except Sale.DoesNotExist:
        print(f"Sale with id {sales_id} does not exist")
        return False
