from django.contrib import admin

# Register your models here.
from .models import Customer,TypeApproval


admin.site.register(Customer)
admin.site.register(TypeApproval)