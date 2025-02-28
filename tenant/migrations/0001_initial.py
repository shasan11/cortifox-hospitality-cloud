# Generated by Django 5.0.7 on 2024-07-31 07:29

import django.db.models.deletion
import django_tenants.postgresql_backend.base
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('schema_name', models.CharField(db_index=True, max_length=63, unique=True, validators=[django_tenants.postgresql_backend.base._check_schema_name])),
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='client')),
                ('name', models.CharField(max_length=255, verbose_name='Client Name')),
                ('nickname', models.CharField(max_length=255, verbose_name='Nickname')),
                ('domain', models.CharField(max_length=255, verbose_name='Domain')),
                ('legal_account', models.CharField(max_length=255, verbose_name='Legal Account')),
                ('is_vat', models.BooleanField(default=False, verbose_name='VAT Registered')),
                ('when_formed', models.DateField(verbose_name='Formation Date')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(db_index=True, max_length=253, unique=True)),
                ('is_primary', models.BooleanField(db_index=True, default=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='tenant.client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_name', models.CharField(db_index=True, max_length=63, unique=True, validators=[django_tenants.postgresql_backend.base._check_schema_name])),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('last_renewed_date', models.DateField(verbose_name='Last Renewed Date')),
                ('active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_pending_payment', models.BooleanField(default=False, verbose_name='Pending Payment')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.client', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
