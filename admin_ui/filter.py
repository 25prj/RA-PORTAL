import django_filters
import django_filters.widgets
from accounts.models import *
from django import forms

#creating a class for filtering the queries

#filter class for type approvals
class typeApprovalFilter(django_filters.FilterSet):

    customer = django_filters.CharFilter(
        #lookup_expr= 'icontains',
        label = 'Customer',
        widget = forms.TextInput(attrs={
            'class':'form-input block w-full rounded-md border-gray-200 shadow-md focus:border-indigo-500 focus:ring-indigo-500',
            'placeholder':'Filter by Customer'
        })
    )

    company_name = django_filters.CharFilter(
        lookup_expr='icontains',
        label = 'Company',
        widget = forms.TextInput(attrs={
            'class':'form-input block w-full rounded-md border-gray-200 shadow-md focus:border-indigo-500 focus:ring-indigo-500',
            'placeholder':'Filter by company...'
        })
    )

    product_type = django_filters.CharFilter(
        lookup_expr='icontains',
        label = 'Product Type',
        widget = forms.TextInput(attrs={
            'class': 'form-input block rounded-md border-gray-200 shadow-md focus:border-indigo-500 focus:ring-indigo-500',
            'placeholder': 'Filter by product type...'
        })
    )

    

    #status
    status = django_filters.ChoiceFilter(
        choices = TypeApproval.STATUS,
        empty_label = "All Statuses",
        widget = forms.Select(attrs={
            'class': 'form-select block w-40 p-2 rounded-md border-gray-300 shadow-md focus:border-indigo-500 focus:ring-indigo-500',

        })
    )
    class Meta:
        model = TypeApproval
        fields = ('customer','company_name','product_type','status')



#dealership license filter 

class DealershipLicenseFilter(django_filters.FilterSet):
    class Meta:
        model = DealershipLicense
        fields = ('customer', 'reg_company_name', 'date', 'status')


    customer = django_filters.CharFilter(
    #lookup_expr= 'icontains',
    label = 'Customer',
    widget = forms.TextInput(attrs={
        'class':'form-input  block w-full rounded-md border-gray-200 shadow-md focus:border-indigo-500 focus:ring-indigo-500',
        'placeholder':'Filter by Customer'
    })
    )

    reg_company_name = django_filters.CharFilter(
        label='Company Name',
        widget = forms.TextInput(attrs={
            'class':'form-input  block w-full rounded-md border-gray-200 shadow-md focus:border-indigo-500 focus:ring-indigo-500',
            'placeholder':'Filter by Company Name',
        })
    )

    date = django_filters.DateFilter(
        label='Date',
        widget = forms.DateInput(attrs={
           'class':'form-input  block w-full rounded-md border-gray-200 shadow-md focus:border-indigo-500 focus:ring-indigo-500',
           'placeholder':'yyyy/mm/dd', 
           'type':'date'
        }, format='%Y-%m-%d')
    )

    status = django_filters.ChoiceFilter(
        choices = DealershipLicense.STATUS,
        empty_label = "All Statuses",
        widget = forms.Select(attrs={
            'class': 'form-select  block w-40 p-2 rounded-md border-gray-300 shadow-md focus:border-indigo-500 focus:ring-indigo-500',

        })
    )