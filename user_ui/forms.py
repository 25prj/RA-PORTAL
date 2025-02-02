from django import forms 
from . models import TypeApproval
from phonenumber_field.formfields import PhoneNumberField

class TypeApprovalForm(forms.ModelForm):
    class Meta:
        model = TypeApproval
        fields = "__all__"

        company_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
            'class':''
        }))

        contact_person = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
            'class':''
        }))

        postal_address = forms.CharField(max_length=100, widget=forms.Textarea(attrs={
            'class':''
        }))

        phone_no = PhoneNumberField()

    




