from django import forms 
from . models import TypeApproval

class TypeApprovalForm(forms.ModelForm):
    class Meta:
        model = TypeApproval
        fields = "__all__"


    
    




