from django import forms 
from accounts.models import TypeApproval


class TypeApprovalForm(forms.ModelForm):
    class Meta:
        model = TypeApproval
        fields = ('status',)

    status = forms.CharField(max_length=100, widget=forms.Select(choices=TypeApproval.STATUS, attrs={
        'class':'py-2 px-2 w-1/2 font-light  text-xl'
    }))  