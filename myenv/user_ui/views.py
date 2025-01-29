from django.shortcuts import render,redirect
from . forms import TypeApprovalForm
from django.utils import timezone
from accounts.decorators import unauthenticated_user,user_authentication


@user_authentication
def TypeApproval_page(request):
    form = TypeApprovalForm()
    if request.method == 'POST':
        form = TypeApprovalForm(request.POST)
        if form.is_valid():
            type_approval_instance = form.save(commit=False)
            type_approval_instance.issue_date = timezone.now()
            type_approval_instance.fax_no = request.POST.get('fax_no', 'N/A')
            type_approval_instance.save()
            return redirect('/')
        else:
            print('invalid form', form.errors)
    else:
        form = TypeApprovalForm()
        return render(request,'user_ui/type_approval.html', {'form': form})
    
    return render(request,'user_ui/type_approval.html')