from django.shortcuts import render
from accounts.decorators import admin_only,allowed_users
# Create your views here.

@admin_only
def admin_ui(request):

    return render(request, 'admin_ui/admin_ui.html')

@admin_only
def dashboard(request):
    return render(request,'admin_ui/dashboard.html')

