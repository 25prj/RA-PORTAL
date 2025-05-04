from django import forms 
from accounts.models import TypeApproval
from phonenumber_field.formfields import PhoneNumberField
from django.utils import timezone


class TypeApprovalForm(forms.ModelForm):
    class Meta:
        model = TypeApproval
        #fields = "__all__"
        exclude = ['status']


    company_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    contact_person = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    
    postal_address = forms.CharField(max_length=255, widget=forms.Textarea(attrs={

        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    phone_no = PhoneNumberField()
    
    phone_no2 = PhoneNumberField()

    fax_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))
    
    alt_email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))


    product_type = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    brand_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    model_no = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    product_no = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    product_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    software_version = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    antenna_type = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    antenna_gain = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    technical_variants = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))


    issue_body = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    issue_date = forms.CharField(widget=forms.DateInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500",

        'placeholder':'yyyy-mm-dd'
    }))


    validity = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))


    emc = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    radio = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    health_and_safety = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

