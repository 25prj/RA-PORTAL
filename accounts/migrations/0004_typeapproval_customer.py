# Generated by Django 5.1.2 on 2025-03-06 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_typeapproval'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeapproval',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customer'),
        ),
    ]
