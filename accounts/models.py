from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError



ext_validator = FileExtensionValidator(['pdf', 'png ', 'jpeg','jpg'])

# custom tin_number_checker

def tin_number_checker(value):
    if not value.startswith('C'):
        raise ValidationError('TIN number should start with a C')
    elif len(value) != 11:
        raise ValidationError('TIN number is 11 digit number')



class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) 
    
    def __str__(self):
        return f"{self.user}"



    
class TypeApproval(models.Model):
    STATUS = (
        ('submitted', 'submitted'),
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



class DealershipLicense(models.Model):
    CLASSCHOICES = {
        'class A': 'CLASS A',
        'class B': 'CLASS B',
        'class C': 'CLASS C',
        'class D': 'CLASS D'
    }

    STATUS = (
        ('submitted', 'submitted'),
        ('under review', 'under review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    )
   
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True, blank=True)
    cls_options = models.CharField(max_length=10, choices=CLASSCHOICES, default="Choose your Class")

    equipments = models.CharField(max_length=250)
    

    #CORPORATE PROFILE
    reg_company_name = models.CharField(max_length=250)
    reg_trade_name = models.CharField(max_length=250)
    reg_company_num = models.CharField(max_length=8,null=True, blank=True)
    tin_num = models.CharField(max_length=11,null=True, blank=True)
    incorporation_date = models.DateField(null=True, blank=True)
    commencement_date = models.DateField(null=True, blank=True)
    district = models.CharField(max_length=250)
    town = models.CharField(max_length=250)
    region = models.CharField(max_length=250)
    postal_addr = models.CharField(max_length=250)
    gps = models.CharField(max_length=250)
    tele_num =PhoneNumberField(blank=True, null=True)
    phone_num = PhoneNumberField(blank=True,null=True)
    site = models.URLField(blank=True, null=True)
    fax =  models.CharField(max_length=250, blank=True, null=True)

    #contact information
    auth_rep_name = models.CharField(max_length=250)
    auth_rep_tele_num =  PhoneNumberField(blank=True, null=True)
    email = models.EmailField()


    #ownership structure
    shareholder_name = models.CharField(max_length=250)
    sharehold = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    shareholder_tin_num = models.CharField(max_length=11,null=True, blank=True, validators=[tin_number_checker])

    #directors
    d_name = models.CharField(max_length=250)
    d_nationality = models.CharField(max_length=250)
    d_address = models.CharField(max_length=250)
    d_tin_num = models.CharField(max_length=11,null=True, blank=True)


    # evidence of company REgistration
    incorporation_cert = models.FileField(upload_to="dealershipFolder")
    commence_cert = models.FileField(upload_to="dealershipFolder", validators=[ext_validator])
    share_cert = models.FileField(upload_to="dealershipFolder", validators=[ext_validator])
    gipc_cert = models.FileField(upload_to="dealershipFolder", validators=[ext_validator])
    tax_cert = models.FileField(upload_to="dealershipFolder", validators=[ext_validator])
    ssnit_cert = models.FileField(upload_to="dealershipFolder", validators=[ext_validator])
    afiliate_cert = models.FileField(upload_to="dealershipFolder", validators=[ext_validator])

    #Profile of technical staff
    tech_stuff = models.FileField(upload_to='dealershipFolder')

    # Business plan 
    company_profile_atch = models.FileField(upload_to="dealershipFolder", validators=[ext_validator])

    #marketing Plane
    market_plan_atch =  models.FileField(upload_to="dealershipFolder", validators=[ext_validator])

    #Financial REport
    financial_report_atch =  models.FileField(upload_to="dealershipFolder", validators=[ext_validator])
    bank_receipt = models.FileField(upload_to="dealershipFolder", validators=[ext_validator])

    # Employee count
    num_employee = models.IntegerField(null=True, blank=True)
    num_employee_props = models.IntegerField(null=True, blank=True) #number of employees proposed
    
    oath = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)

    passport = models.ImageField(upload_to='passports',validators=[ext_validator])

    status = models.CharField(max_length=50, choices=STATUS, default='submitted')
    

    def __str__(self):
        return f"Dealership License for {self.reg_company_name}"

