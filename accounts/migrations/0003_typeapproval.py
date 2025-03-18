# Generated by Django 5.1.2 on 2025-03-06 08:12

import django.utils.timezone
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customer_password1_remove_customer_password2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=100)),
                ('postal_address', models.TextField(max_length=255)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('phone_no2', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('fax_no', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('alt_email', models.EmailField(max_length=100)),
                ('product_type', models.CharField(max_length=100)),
                ('brand_name', models.CharField(max_length=100)),
                ('model_no', models.CharField(max_length=50)),
                ('product_no', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=100)),
                ('software_version', models.CharField(max_length=100)),
                ('antenna_type', models.CharField(max_length=100)),
                ('antenna_gain', models.CharField(max_length=100)),
                ('technical_variants', models.CharField(max_length=100)),
                ('issue_body', models.CharField(max_length=100)),
                ('issue_date', models.DateField(default=django.utils.timezone.now)),
                ('validity', models.CharField(max_length=50)),
                ('emc', models.TextField(max_length=255)),
                ('radio', models.TextField(max_length=255)),
                ('health_and_safety', models.TextField(max_length=255)),
            ],
        ),
    ]
