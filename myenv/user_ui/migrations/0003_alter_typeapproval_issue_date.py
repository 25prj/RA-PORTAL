# Generated by Django 5.1.2 on 2025-01-28 10:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_ui', '0002_alter_typeapproval_phone_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeapproval',
            name='issue_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
