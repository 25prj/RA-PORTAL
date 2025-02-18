from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Username",
        'class':'py-2 px-2 w-full focus:outline-none focus'
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
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Last Name",
        'class':'py-2 px-2 w-full focus:outline-none'
    }))



    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Username",
        'class':'py-2 px-2 w-full focus:outline-none'
    }))
    
    company = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Company",
        'class':'py-2 px-2 w-full focus:outline-none'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "example@gmail.com",
        'class':'py-2 px-2 w-full focus:outline-none'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "password",
        'class':'py-2 px-2 w-full focus:outline-none'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "confirm password",
        'class':'py-2 px-2 w-full focus:outline-none'
    }))






