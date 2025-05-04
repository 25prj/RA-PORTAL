from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Customer

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Username",
        'class':'py-2 px-2 w-full focus:outline-none'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "password",
        'class':'py-2 px-2 w-full focus:outline-none'
    }))


    

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','company', 'email', 'password1', 'password2']


    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "First Name",
        'class':'py-2 px-2 w-full focus:outline-none'
    }), label="", help_text="<span class='font-small text-gray-500'><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_only</small></span>")
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Last Name",
        'class':'py-2 px-2 w-full focus:outline-none'
    }), label="", help_text="<span class='font-small text-gray-500'><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_only</small></span>")



    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Username",
        'class':'py-2 px-2 w-full focus:outline-none'
    }),label="", help_text="<span class='font-small text-gray-500'><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_only</small></span>")
    
    company = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Company",
        'class':'py-2 px-2 w-full focus:outline-none'
    }), label='',  help_text="<span class='font-small text-gray-500'><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_only</small></span>")

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "example@gmail.com",
        'class':'py-2 px-2 w-full focus:outline-none'
    }),label="")

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "password",
        'class':'py-2 px-2 w-full focus:outline-none my-4'
    }),label='',help_text = '<ul class="font-small text-gray-500"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>')

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "confirm password",
        'class':'py-2 px-2 w-full focus:outline-none mb-4'
    }),label='',)






