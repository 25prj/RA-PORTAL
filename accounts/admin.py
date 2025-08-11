from django.contrib import admin

# Register your models here.
from .models import Customer,TypeApproval,DealershipLicense


admin.site.register(Customer)
admin.site.register(TypeApproval)
admin.site.register(DealershipLicense)