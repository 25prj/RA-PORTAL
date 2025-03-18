from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import LoginForm,SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .decorators import unauthenticated_user, admin_only
from django.contrib.auth.models import User
from .models import Customer

# Create your views here.

@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)
        Customer.objects.get_or_create(user=user)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('admin')
            else:
                return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
            
            return render(request,'accounts/signin.html',{'form':LoginForm()})
        
    return render(request, 'accounts/signin.html', {'form': LoginForm()})

@unauthenticated_user
def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        company= request.POST.get('company')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if len(username) < 3: #check if username is less than 3 characters
            messages.error(request, 'username should be 3 characters or more.')
        elif User.objects.filter(email=email).exists(): #check if email already exists
            messages.error(request, f'This email has an account already exists.')
            
        elif len(password1) < 8:
            messages.error(request, 'Password is less than 8 characters.')
        elif password1 != password2:
            messages.error(request, 'Passwords do not match.')
        else:
            password = request.POST.get('password2')
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password1,
            )
            
            group = Group.objects.get(name='customer')
            #print(f'group name: {group.name}')
            group2 = Group.objects.get(name='admin')
            
            if 'sakara' in email:
                user.is_superuser = True
                user.groups.add(group2)
                user.save()
            else:
                user.groups.add(group)
                user.save()
               

            return redirect('accounts:login')
    
    return render(request, 'accounts/signup.html',{'form': SignupForm()})


def warning_page(request):
    return render(request, 'accounts/warning.html')

def logout_user(request):
    logout(request)

    return redirect('/')
    