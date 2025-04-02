from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
   
    


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class TypeApproval(models.Model):
    STATUS = (
        
        ('under review', 'under review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    )

    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    postal_address = models.TextField(max_length=255)
    phone_no = PhoneNumberField()
    phone_no2 = PhoneNumberField()
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
    issue_date = models.DateField(default=timezone.now)
    validity = models.CharField(max_length=50)

    emc = models.TextField(max_length=255)
    radio = models.TextField(max_length=255)
    health_and_safety = models.TextField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS, default='submitted')


    def __str__(self):
        return self.company_name

