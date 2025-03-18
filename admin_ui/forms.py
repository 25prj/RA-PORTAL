from django import forms 
from accounts.models import TypeApproval


class TypeApprovalForm(forms.ModelForm):
    class Meta:
        model = TypeApproval
        fields = ('status',)

    status = forms.CharField(max_length=100, widget=forms.Select(choices=TypeApproval.STATUS))  