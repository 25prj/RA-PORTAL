from django.shortcuts import render,redirect,get_object_or_404
from .forms import TypeApprovalForm, CompanyInfoForm,ProductInfoForm,ApprovalDetailsForm, serviceOptionForm, corporateProfileForm,  contactInformationForm, ownershipForm, directorsForm, evidenceForm, businessForm, othersForm 
from accounts.decorators import users_authentication
from django.utils import timezone
#from .models import TypeApproval
from accounts.models import TypeApproval,DealershipLicense
from django.core.paginator import Paginator
from django.views.generic import View
from django.urls import reverse
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from phonenumbers import format_number, PhoneNumberFormat


#from phonenumber_field.phonenumber import PhoneNumber, PhoneNumberFormat
# form wizard
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponse

import json
from datetime import date


   
# form wizard view class

class TypeApprovalView(View):
    
    template_name = 'user_ui/type_approval_form.html'

    def get_redirect_url(self, step):
        """Helper method to generate redirect URL with step parameter"""
        return f"{reverse('user_ui:type_approval_form')}?step={step}"
    
     
    def get(self,request):
        if request.user.is_authenticated:

            step = request.GET.get('step','1')

            if step == '1':
                form = CompanyInfoForm()
            elif step == '2':
                form = ProductInfoForm()
            elif step == '3':
                form = ApprovalDetailsForm()
            else:
                return redirect(self.get_redirect_url('1'))
            

            # Load data from session if available
            form_data = request.session.get('form_data', {}) or {}
            for field, value in form_data.items():
                try:
                    if field in form.fields:
                        form.fields[field].initial = value 
                except KeyError:
                    continue

            
            return render(request,self.template_name,{
                'form':form,
                'step':step,
                'total_steps':3
            })
        else:
            return redirect('accounts:login')
    
   
    def post(self, request):
        if request.user.is_authenticated:

            step = request.POST.get('step','1')

            if 'form_data' not in request.session:
                request.session['form_data'] = {}


            if step == '1':
                form = CompanyInfoForm(request.POST)
                if form.is_valid():
                    clean_data = form.cleaned_data
                    if 'phone_no' in clean_data and 'phone_no2' in clean_data:
                        clean_data['phone_no'] = format_number(clean_data['phone_no'], PhoneNumberFormat.E164)
                        clean_data['phone_no2'] = format_number(clean_data['phone_no2'], PhoneNumberFormat.E164)

                    request.session['form_data'].update(clean_data)
                    request.session.modified = True 

                    return redirect(self.get_redirect_url('2'))
                
            elif step == '2':
                form = ProductInfoForm(request.POST)
                if form.is_valid():
                    clean_data = form.cleaned_data
                    request.session.modified = True 
                    request.session['form_data'].update(clean_data)

                    return redirect(self.get_redirect_url('3'))
            elif step == '3':
                form = ApprovalDetailsForm(request.POST)
                if form.is_valid():
                    clean_data = form.cleaned_data 
                    
                    request.session['form_data'].update(clean_data)
                    request.session.modified = True 

                    try:
                        
                        form_data = request.session['form_data']
                        type_approval_instance = TypeApproval(**form_data)
                        
                        type_approval_instance.customer = request.user.customer
                        type_approval_instance.save()
                    
                        print('------------------- Data collected ---------------\n')
                        print(form_data)
                        print(f'\n{type_approval_instance}')

                        del request.session['form_data']
                        #del form_data
                    
                        #return redirect('user_ui:success-page')
                        return redirect('user_ui:success-page')
                    except KeyError as e:
                        form.add_error(None, f"Database error: {e}")
                    
            return render(request,self.template_name,{
                'form':form,
                'step':step,
                'total_steps':3
            })
        
        else:
            return redirect('accounts:login')







'''
@users_authentication
#the view function fro type approval form
def type_approval_view(request):
    if request.method == 'POST':
        form = TypeApprovalForm(request.POST)
        print(form)
        if form.is_valid():
            type_approval_instance = form.save(commit=False)
            type_approval_instance.issue_date = timezone.now()
            type_approval_instance.fax_no = request.POST.get('fax_no', 'N/A')
            type_approval_instance.customer = request.user.customer
            type_approval_instance.save()

            return redirect("user_ui:success-page")
        else:
            print('form is invalid', form.errors)
    else:
        form = TypeApprovalForm()

    return render(request,'user_ui/type_approval.html', {'form':form})
'''



# dealership license form func
@users_authentication
def dealership(request):
    return render(request,'user_ui/dealership-form.html')



class dealershipView(LoginRequiredMixin,View):

    
    template_name = 'user_ui/dealership_form.html'

    def get_redirect_url(self, step):
        """Helper method to generate redirect URL with step parameter"""
        return f"{reverse('user_ui:dealershipForm')}?step={step}"

    
    def get(self, request):
        

        step = request.GET.get('step', '1')

        if step == '1':
            form = serviceOptionForm()
        elif step == '2':
            form = corporateProfileForm()
        elif step == '3':
            form = contactInformationForm()
        elif step == '4':
            form = ownershipForm()
        elif step == '5':
            form = directorsForm()
        elif step == '6':
            form = evidenceForm()
        elif step == '7':
            form = businessForm()
        elif step == '8':
            form = othersForm()
        else:
            return redirect(self.get_redirect_url('1'))
        

        dealership_form_data = request.session.get('dealership_form_data', {}) or {}
        for field, value in dealership_form_data.items():
            try:
                if field in form.fields:
                    form.fields[field].initial = value
            except KeyError:
                continue
        
        return render(request, self.template_name,{
            'step':step,
            'form':form,
            'total_steps':8
        })
    

    
    
    def post(self, request):
        
        step = request.POST.get('step','1')
        if 'dealership_form_data' not in request.session:
            request.session['dealership_form_data'] = {}


        if step == '1':
            form = serviceOptionForm(request.POST)
            if form.is_valid():
                clean_data = form.cleaned_data
                request.session['dealership_form_data'].update(clean_data)
                request.session.modified = True 

                print('------------------- Data collected ---------------\n')
                print(f'\n{request.session['dealership_form_data']}')
                return redirect(self.get_redirect_url('2'))
            
        elif step == '2':
            form = corporateProfileForm(request.POST)
            if form.is_valid():
                clean_data = form.cleaned_data
                #serializing tele_num and phone_num to json format to able to save in session.
                if 'tele_num' in clean_data and 'phone_num' in clean_data:
                    clean_data['tele_num'] = format_number(clean_data['tele_num'], PhoneNumberFormat.E164)
                    clean_data['phone_num'] = format_number(clean_data['phone_num'], PhoneNumberFormat.E164)
                request.session['dealership_form_data'].update(clean_data)
                request.session.modified = True 

                print('------------------- Data collected ---------------\n')
                print(f'\n{request.session['dealership_form_data']}')

                return redirect(self.get_redirect_url('3'))

        elif step == '3':
            form = contactInformationForm(request.POST)
            if form.is_valid():
                clean_data = form.cleaned_data
                if 'auth_rep_tele_num' in clean_data:
                    clean_data['auth_rep_tele_num'] =  format_number(clean_data['auth_rep_tele_num'], PhoneNumberFormat.E164)
                request.session['dealership_form_data'].update(clean_data)
                request.session.modified = True 

                print('------------------- Data collected ---------------\n')
                print(f'\n{request.session['dealership_form_data']}')

                return redirect(self.get_redirect_url('4'))
            
        elif step == '4':
            form = ownershipForm(request.POST)
            if form.is_valid():
                clean_data = form.cleaned_data
                request.session['dealership_form_data'].update(clean_data)
                request.session.modified = True 

                print('------------------- Data collected ---------------\n')
                print(f'\n{request.session['dealership_form_data']}')

                return redirect(self.get_redirect_url('5'))
            
        elif step == '5':
            form = directorsForm(request.POST)
            if form.is_valid():
                clean_data = form.cleaned_data
                request.session['dealership_form_data'].update(clean_data)
                request.session.modified = True 

                print('------------------- Data collected ---------------\n')
                print(f'\n{request.session['dealership_form_data']}')

                return redirect(self.get_redirect_url('6'))
            
        elif step =='6':
            form = evidenceForm(request.POST, request.FILES)
            if form.is_valid():
                clean_data = form.cleaned_data
                
                file_object_values = []
                for key,value in clean_data.items():
                    if key in clean_data and clean_data[key]:
                        upload_file_object = clean_data[key]
                        file_object_values.append(value)

                        if upload_file_object in file_object_values:
                            save_file_path = default_storage.save(
                                upload_file_object.name, 
                                upload_file_object
                            )

                            clean_data[key] = save_file_path
                    
                    else:
                        clean_data = None 

                
                request.session['dealership_form_data'].update(clean_data)
                request.session.modified = True 

                print('------------------- Data collected ---------------\n')
                print(f'\n{request.session['dealership_form_data']}')

                return redirect(self.get_redirect_url('7'))
            
        elif step == '7':
            form = businessForm(request.POST, request.FILES)
            if form.is_valid():
                clean_data = form.cleaned_data
                file_object_values = []
                
                for key, value in clean_data.items():
                    if key in clean_data and clean_data[key]:
                        upload_file_object = clean_data[key]
                        file_object_values.append(value)

                        if upload_file_object in file_object_values:
                            save_file_path = default_storage.save(
                                upload_file_object.name, 
                                upload_file_object
                            )

                            clean_data[key] = save_file_path
                
                    else:
                        clean_data = None 


                request.session['dealership_form_data'].update(clean_data)
                request.session.modified = True 

                print('------------------- Data collected ---------------\n')
                print(f'\n{request.session['dealership_form_data']}')
                return redirect(self.get_redirect_url('8'))
                
        elif step == '8':
            form = othersForm(request.POST, request.FILES)
            if form.is_valid():
                clean_data = form.cleaned_data.copy() 

                if 'passport' in clean_data and clean_data['passport']:
                    upload_file_object = clean_data['passport']
                    save_file_path = default_storage.save(
                        upload_file_object.name, 
                        upload_file_object
                    )

                    clean_data['passport'] = save_file_path
                else:
                    clean_data.pop('passport', None) # just remove passport if not present
                

                request.session['dealership_form_data'].update(clean_data)
                request.session.modified = True 
                
                try:
                    form_data = request.session['dealership_form_data']
                    dealership_instance = DealershipLicense(**form_data)

                    dealership_instance.customer = request.user.customer 
                    dealership_instance.save()
                    dealership_instance.customer.save()

                    print('------------------- Data collected ---------------\n')
                    print(f'\n{form_data}')
                    print(f'\n{dealership_instance}')
                    print(dealership_instance.customer)

                    del request.session['dealership_form_data']

                    
                    return redirect('user_ui:success-page')    
                except KeyError as e:
                    form.add_error(None, f"Database error: {e}") 
                    print('form is not stoed into the database')    
    
        return render(request, self.template_name, {
            'form':form,
            'step':step,
            'total_steps':8
        })

                   
                    
                        
# Dealership list view, showing table of customer dealership license 
# application
# dealership list view page

def dealership_license_list(request):
    # query for all dealership license relate to each customer 
    dealership_licenses = request.user.customer.dealershiplicense_set.all() 

    # setting pagination for table
    pagination = Paginator(dealership_licenses, 5) # show 5 items per page
    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)

    nums = "a" * page_obj.paginator.num_pages
    
    context = {
        'dealership_applications':dealership_licenses,
        'page_obj':page_obj,
        'nums':nums
        
    }
    return render(request,'user_ui/dealership_list.html', context)


# dealership license view page
# view from table or full view of license application

def dealership_license_view(request, pk):
    details = DealershipLicense.objects.get(id=pk)

    context = {
        'details':details,
        
    }
    return render(request, 'user_ui/dealership_view.html', context)
                


                

def success_page(request):
    return render(request,'user_ui/success.html')



#view func for type for type approvals submitted
@users_authentication
def type_approval_list(request):
    type_approvals = request.user.customer.typeapproval_set.all()
    #costumer = TypeApproval.objects.get(id=3)
    first_name = request.user.first_name
    last_name = request.user.last_name
    
    print(type_approvals)
    

    for approval in type_approvals:
        print('this is type approval ')
        print(f'{approval.company_name} Date: {approval.issue_date}')

    #setting pagination
    p = Paginator(type_approvals,5)
    page = request.GET.get('page')
    type_list = p.get_page(page)

    nums  = "a" * type_list.paginator.num_pages

    return render(request,'user_ui/my_approvals.html', {
        'type_approvals':type_approvals,
        'type_list': type_list,
        'nums':nums,
    })



def approval_view(request,approval_id):
    #type_approvals = get_object_or_404(TypeApproval, id=view_id)
    app_details= TypeApproval.objects.get(id=approval_id)
    if request.method == 'POST':
        form = TypeApprovalForm(request.POST or None,instance=app_details) 
        if form.is_valid():
            form.save()
            
            #return redirect('type-approval')
    else:
        form = TypeApprovalForm(instance=app_details)
        print('not save')
    context = {
        'app_details':app_details,
        'form':form
    }
    

    return render(request, 'user_ui/approval_view.html', context)


# updating an approval
def approval_edit(request, approval_id):

    current_approval_page = TypeApproval.objects.get(id=approval_id)
    if request.method == 'POST':
        form = TypeApprovalForm(request.POST or None, instance=current_approval_page)
        
        
        if form.is_valid():
            form.save()
            
            return redirect('user_ui:type-approval-list')
    else:
        form = TypeApprovalForm(instance=current_approval_page)
        
        return render(request, 'user_ui/approval_edit.html', context={
            'form':form,
            
        })
    
    return render(request, 'user_ui/approval_edit.html', context={
        #'form':form,
        'current_approval_page':current_approval_page
    })