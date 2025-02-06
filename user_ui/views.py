from django.shortcuts import render,redirect
from .forms import TypeApprovalForm
from accounts.decorators import users_authentication
from django.utils import timezone
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