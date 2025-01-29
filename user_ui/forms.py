from django import forms 
from . models import TypeApproval

class TypeApprovalForm(forms.ModelForm):
    class Meta:
        model = TypeApproval
        fields = "__all__"


    company_name = forms.CharField(max_length=)
    




