from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from .forms import LoginForm,SignupForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .decorators import unauthenticated_user, admin_only
from django.contrib.auth.models import User
from .models import Customer
from .utils import send_otp
from datetime import datetime
import pyotp

from django.contrib.auth import update_session_auth_hash

# Create your views here.

@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)
        Customer.objects.get_or_create(user=user)

        request.session['username'] = request.POST.get('username')
        request.session['password'] = request.POST.get('password')
        request.session['email'] = request.POST.get('email')
        email = request.POST.get('email')
        username = request.POST.get('username')


        if user is not None:
            send_otp(request,username)
            #login(request, user)
            

            '''
            if user.is_superuser:
                return redirect('admin')
            else:
                return redirect('/')
            '''
            
            return redirect('accounts:otp-page')
        else:
            messages.error(request, 'Invalid username or password')
            
            return render(request,'accounts/signin.html',{'loginform':LoginForm()})
        
    return render(request, 'accounts/signin.html', {'loginform': LoginForm()})


#OTP 
def otp_view(request):
    if request.method == 'POST':
        otp = request.POST["otp"]
        otp_secret_key = request.session['otp_secret_key']
        otp_valid_date = request.session['otp_valid_date']

        
        
        username = request.session['username']
        password = request.session['password']
        #email = request.session['email']


        if otp_secret_key and otp_valid_date is not None:
            valid_until = datetime.fromisoformat(otp_valid_date)
            print(f"formatted date VALID UNTIL: {valid_until}")
            print(f"date now: {datetime.now()}")

            if datetime.now() < valid_until:
                totp = pyotp.TOTP(otp_secret_key, interval=120)
                
                if totp.verify(otp):
                    user = authenticate(request,username=username, password=password)
                    Customer.objects.get_or_create(user=user)
                    
                    login(request, user)

                    messages.success(request, f'You are logged in as {user.username}')
                    
                    del request.session['otp_secret_key']
                    del request.session['otp_valid_date']
                    
                    if user.is_superuser:
                        return redirect('admin')
                    else:
                       
                        return redirect ('/')
                    
                
                
                else:
                    print('invalid otp')
                    messages.success(request, f'Invalid otp code!!!')
            else:
                print('otp expired')
        else:
            print('something went wrong...')

            
    return render(request, 'accounts/otp-page.html',)


@unauthenticated_user
def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            #user = User.objects.create_user(username=username, email=email, password=password)
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
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
            

            #messages.success(request, 'Account created successfully!')
            return redirect('accounts:login')
        
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

    '''
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
    '''

# changing user's password
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            print('\n password resetted')
            
            update_session_auth_hash(request, form.user)

            return redirect('accounts:login')
        else:
            print('\n password not resetted!!')
    else:
        form = PasswordChangeForm()
        return render(request, 'accounts/password_change.html',context={
            'form':form
        })
    
    return render(request,'accounts/password_change.html', context={
        'form':form,
    })


def warning_page(request):
    return render(request, 'accounts/warning.html')

def logout_user(request):
    logout(request)

    return redirect('/')
    