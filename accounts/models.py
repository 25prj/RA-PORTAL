from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    company = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.first_name} {self.last_name} >> {self.username}"
    
    
    

