from django.shortcuts import render
from accounts.decorators import admin_only
# Create your views here.

@admin_only
def admin_ui(request):

    return render(request, 'admin_ui/admin_ui.html')