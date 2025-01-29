from django import forms 
from . models import TypeApproval
from phonenumber_field.formfields import PhoneNumberField

class TypeApprovalForm(forms.ModelForm):
    class Meta:
        model = TypeApproval
        fields = ['company_name', 'phone_no', 'email']

        company_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class':''
        }), label="Company Name")

        phone_no = PhoneNumberField(label="Phone Number")
        
        email = forms.EmailField(max_length=100,widget=forms.TextInput(attrs={
            'class':''
        }), label="Email")


    
    

    
    










