from django.shortcuts import render,redirect,get_object_or_404
from accounts.decorators import admin_only,allowed_users
from user_ui.models import TypeApproval
from django.http import HttpResponse
# Create your views here.

from accounts.models import Customer,TypeApproval, DealershipLicense
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .forms import TypeApprovalForm,AddingUser,DealershipLicenseResponseForm
from .filter import typeApprovalFilter, DealershipLicenseFilter
from django.contrib import messages
#import paginator
from django.core.paginator import Paginator



@admin_only
def admin_ui(request):
    type_approvals = TypeApproval.objects.all()
    type_approvals_count = type_approvals.count()

    #dealership count: number of dealership license applied
    dealership_licenses = DealershipLicense.objects.all()
    dealership_licenses_count = dealership_licenses.count()

    
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
        'dealership_licenses_count':dealership_licenses_count,
        
    }

    return render(request, 'admin_ui/admin_ui.html', context)

@admin_only
def dashboard(request):
    return render(request,'admin_ui/dashboard.html')

#generating a text file
def type_approval_textFile(request):
    response = HttpResponse(content_type = 'text/plain')
    response['Content-Disposition'] = 'attachment; filename=type_approval.txt'
    approvals = TypeApproval.objects.all()

    # Create a list to hold the lines of text 
    lines = []
    #looping thru
    for approval in approvals:
        lines.append(f"{approval}\n")
    
    
    #Write the lines to the response
    response.writelines(lines)
    return response

#showing type approval list in table form from admin side
@admin_only
def type_approval(request):
    type_approval_list = TypeApproval.objects.all().order_by('-issue_date')
    #customers = Customer.objects.all()
    
    #filter or search for typeapprovals
    myFilter = typeApprovalFilter(request.GET, queryset=type_approval_list)
    type_approval_list = myFilter.qs 

    #set up pagination  
    p = Paginator(type_approval_list,6)
    page = request.GET.get('page')
    type_list = p.get_page(page)

    nums  = "a" * type_list.paginator.num_pages
    
    
    context = {
        'type_approval_list':type_approval_list,
        #'customers':customers,
        'myFilter':myFilter,
        'type_list':type_list,
        'nums':nums
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


#deleting type approvals
@admin_only
def delete_approval(request,pk):
    approval = TypeApproval.objects.get(id=pk)
    if request.method == 'POST':
        approval.delete()

        messages.success(request, f'{approval.company_name} is deleted successfully...')
        return redirect('type-approval')
    
    context = {
        'approval':approval,
    }
    return render(request, 'admin_ui/delete_approval.html', context)


# showing dealership license list
@admin_only
def dealership_license_list(request):
    dealership_list = DealershipLicense.objects.all().order_by('-date')

    # filter or search for dealership list
    myfilter = DealershipLicenseFilter(request.GET, queryset=dealership_list)
    dealership_list = myfilter.qs

    #setting pagination
    pagination = Paginator(dealership_list, 5)
    page = request.GET.get('page')
    page_obj = pagination.get_page(page)

    nums = "a" * page_obj.paginator.num_pages

    context = {
        'page_obj':page_obj,
        'nums':nums,
        'myfilter':myfilter,
    }
    return render(request,'admin_ui/dealership_list.html', context)


# dealership view details page func
@admin_only
def dealership_view_details(request,view_id):
    dealership_view = get_object_or_404(DealershipLicense,id=view_id)
    if request.method == 'POST':
        form = DealershipLicenseResponseForm(request.POST or None, instance=dealership_view)
        if form.is_valid():
            form.save()

           
            return redirect('dealership_list')
    else:
        form = DealershipLicenseResponseForm(instance=dealership_view)
        #return render(request,'admin_ui/dealershipview_details_page.html', context)
    
    context = {
        'dealership_view':dealership_view,
        'form':form
    }

    return render(request,'admin_ui/dealershipview_details_page.html', context)


#deleting a dealership license from dealership list
@admin_only
def delete_dealership_license(request,pk):
    dealership_license = get_object_or_404(DealershipLicense,id=pk)
    if request.method == 'POST':
        dealership_license.delete()

        messages.success(request, f'{dealership_license.reg_company_name} is deleted successfully')
        return redirect('dealership_list')
    
    
    return redirect(request, '', {'dealership_license':dealership_license})




# managing users
@admin_only
def users_list(request):
    users = User.objects.filter(is_superuser=0).order_by('-date_joined')
    admins = User.objects.filter(is_superuser=1).order_by('-date_joined')

    #setting pagination
    pagination = Paginator(users, 7)
    page = request.GET.get('page')
    users_list = pagination.get_page(page)

    #setting pagination for admin list users
    p = Paginator(admins, 7)
    page2 = request.GET.get('page')
    admins_list = p.get_page(page2)

    nums = 'a' * users_list.paginator.num_pages
    context = {
        'users':users,
        'admins':admins,
        'admins_list':admins_list,
        'users_list':users_list,
        'nums':nums,
    }
    return render(request,'admin_ui/users_list.html', context)


#deleting user
@admin_only
def delete_user(request,pk):
    deleted_user = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        deleted_user.delete()

        messages.success(request, f'User <{deleted_user.first_name} {deleted_user.last_name}> is deleted successfull ')
        return redirect('users-list')
    
    return render(request, '', context={'deleted_user':deleted_user})


# creating or adding a new user
@admin_only
def creating_user(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email  = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        a = first_name[0]

        print(f'\nDebuggin form, fullname: {first_name} {last_name} {a}')
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password = password1
        )

        group = Group.objects.get(name='customer')
        group2 = Group.objects.get(name='admin')

        if 'sakara' in email:
            user.is_superuser = True
            user.groups.add(group2)
            user.save()
        else:
            user.groups.add(group)
            user.save()

        return redirect('users-list')
    
    return render(request, 'admin_ui/creating_user.html')


