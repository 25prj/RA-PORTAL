# Generated by Django 5.1.2 on 2025-01-26 06:52

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_ui', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeapproval',
            name='phone_no',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='typeapproval',
            name='phone_no2',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
