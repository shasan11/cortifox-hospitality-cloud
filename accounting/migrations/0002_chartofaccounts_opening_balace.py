# Generated by Django 5.0.7 on 2024-07-25 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartofaccounts',
            name='opening_balace',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
