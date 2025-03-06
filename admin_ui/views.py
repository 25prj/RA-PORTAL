from django.shortcuts import render
from accounts.decorators import admin_only,allowed_users
from user_ui.models import TypeApproval
# Create your views here.

@admin_only
def admin_ui(request):
    type_approvals = TypeApproval.objects.all()
    type_approvals_count = type_approvals.count()
    return render(request, 'admin_ui/admin_ui.html', {'type_approvals_count':type_approvals_count})

@admin_only
def dashboard(request):
    return render(request,'admin_ui/dashboard.html')

