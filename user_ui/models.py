from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from accounts.models import Customer
# Create your models here.

class TypeApproval(models.Model):
    STATUS = (
        ('pending','pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
    )
    company_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    postal_address = models.TextField(max_length=255)
    phone_no = models.CharField(max_length=10)
    phone_no2 = models.CharField(max_length=10)
    fax_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    alt_email = models.EmailField(max_length=100)

    product_type = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    model_no = models.CharField(max_length=50)
    product_no = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    software_version = models.CharField(max_length=100)
    antenna_type = models.CharField(max_length=100)
    antenna_gain = models.CharField(max_length=100)
    technical_variants = models.CharField(max_length=100)


    issue_body = models.CharField(max_length=100)
    issue_date = models.DateField()
    validity = models.CharField(max_length=50)

    emc = models.TextField(max_length=255)
    radio = models.TextField(max_length=255)
    health_and_safety = models.TextField(max_length=255)

    status = models.CharField(max_length=50, choices=STATUS, default='pending')


    def __str__(self):
        return f"{self.contact_person} from {self.company_name}"
    

class Dealership(models.Model):
    company_name = models.CharField(max_length=50)
    trade_name  = models.CharField(max_length=50)

    date = models.DateField()
    postal_address = models.CharField(max_length=100)
    digital_address = models.CharField(max_length=50)

    
