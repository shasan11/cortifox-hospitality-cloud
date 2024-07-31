from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django_tenants.utils import get_tenant_model, get_tenant_domain_model

class Client(TenantMixin):
    client_id = models.AutoField(primary_key=True)
    pic = models.ImageField(upload_to="client", null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name='Client Name')
    nickname = models.CharField(max_length=255, verbose_name='Nickname')
    domain = models.CharField(max_length=255, verbose_name='Domain')
    legal_account = models.CharField(max_length=255, verbose_name='Legal Account')
    is_vat = models.BooleanField(default=False, verbose_name='VAT Registered')
    when_formed = models.DateField(verbose_name='Formation Date',blank=True,null=True)
    address = models.CharField(max_length=255, verbose_name='Address')
    phone = models.CharField(max_length=20, verbose_name='Phone Number')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date')

    auto_create_schema = True

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Ensure the domain is created after the tenant is saved
        if self.pk:  # Check if the tenant is already saved
            domain_model = get_tenant_domain_model()
            domain, created = domain_model.objects.get_or_create(
                domain=self.domain,
                tenant=self,
                defaults={'is_primary': True}
            )


class Service(TenantMixin):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Client')
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')
    last_renewed_date = models.DateField(verbose_name='Last Renewed Date')
    active = models.BooleanField(default=True, verbose_name='Is Active')
    is_pending_payment = models.BooleanField(default=False, verbose_name='Pending Payment')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date')

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return f"Service for {self.client.name}"


class Domain(DomainMixin):
    pass
