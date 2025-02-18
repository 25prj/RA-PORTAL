from django.shortcuts import render,redirect,get_object_or_404
from .forms import TypeApprovalForm
from accounts.decorators import users_authentication
from django.utils import timezone
from .models import TypeApproval
# Create your views here.

@users_authentication
def type_approval_view(request):
    if request.method == 'POST':
        form = TypeApprovalForm(request.POST)
        if form.is_valid():
            type_approval_instance = form.save(commit=False)
            type_approval_instance.issue_date = timezone.now()
            type_approval_instance.fax_no = request.POST.get('fax_no', 'N/A')
            type_approval_instance.save()

            return redirect("user_ui:success-page")
        else:
            print('form is invalid', form.errors)
    else:
        form = TypeApprovalForm()

    return render(request,'user_ui/type_approval.html', {'form':form})


def success_page(request):
    return render(request,'user_ui/success.html')

@users_authentication
def type_approval_list(request):
    type_approvals = TypeApproval.objects.all()
    #costumer = TypeApproval.objects.get(id=3)
    first_name = request.user.first_name
    last_name = request.user.last_name

    print(type_approvals)
    

    for approval in type_approvals:
        print('this is type approval ')
        print(f'{approval.company_name} Date: {approval.issue_date}')

    return render(request,'user_ui/my_approvals.html', {'type_approvals':type_approvals, 'first_name':first_name, 'last_name':last_name})



def approval_view(request,view_id):
    type_approvals = get_object_or_404(TypeApproval, id=view_id)

    return render(request, 'user_ui/approval_view.html', {'type_approvals':type_approvals})