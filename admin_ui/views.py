from django.shortcuts import render,redirect
from accounts.decorators import admin_only,allowed_users
from user_ui.models import TypeApproval
# Create your views here.

from accounts.models import Customer,TypeApproval
from .forms import TypeApprovalForm
from accounts.filter import typeApprovalFilter

@admin_only
def admin_ui(request):
    type_approvals = TypeApproval.objects.all()
    type_approvals_count = type_approvals.count()
    
    #gets the number of under reviewed applications
    approvals_under_review = TypeApproval.objects.filter(status='under review')

    #gets the number of approved applications
    approved_apps = TypeApproval.objects.filter(status='approved')

    #get the number of rejected applications
    rejected_apps = TypeApproval.objects.filter(status='rejected')


    context = {
        'type_approvals': type_approvals,
        'type_approvals_count': type_approvals_count,
        'approvals_under_review':approvals_under_review.count(),
        'approved_apps':approved_apps.count(),
        'rejected_apps':rejected_apps.count(),
    }

    return render(request, 'admin_ui/admin_ui.html', context)

@admin_only
def dashboard(request):
    return render(request,'admin_ui/dashboard.html')


@admin_only
def type_approval(request):
    type_approval_list = TypeApproval.objects.all()
    #customers = Customer.objects.all()

    #filter or search for typeapprovals
    myFilter = typeApprovalFilter(request.GET, queryset=type_approval_list)
    type_approval_list = myFilter.qs 
    context = {
        'type_approval_list':type_approval_list,
        #'customers':customers,
        'myFilter':myFilter,
    }
    return render(request, 'admin_ui/type_approval.html',context)


# select or able to approve or decline a type approval
@admin_only
def details(request,view_id):
    app_details= TypeApproval.objects.get(id=view_id)
    if request.method == 'POST':
        form = TypeApprovalForm(request.POST or None,instance=app_details) 
        if form.is_valid():
            form.save()
            print('save')
            return redirect('type-approval')
    else:
        form = TypeApprovalForm(instance=app_details)
        print('not save')
    context = {
        'app_details':app_details,
        'form':form
    }
    return render(request,'admin_ui/details.html', context)


