from django import forms 
from accounts.models import TypeApproval


class TypeApprovalForm(forms.ModelForm):
    class Meta:
        model = TypeApproval
        fields = ('status',)

    status = forms.CharField(max_length=100, widget=forms.Select(choices=TypeApproval.STATUS, attrs={
        'class':'py-2 px-2 w-1/2 font-light  text-xl rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 hover:-translate-y-0.5 transform hover:ring-2'
    })) 

    
