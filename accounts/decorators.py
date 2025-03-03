from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

#restrict login users not visit signup and login url
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func


#allowing only admins to visite some sites and restrict users
def admin_only(admin_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return admin_func(request, *args, **kwargs)
        else:
            #return HttpResponse('You are not authorized to view this page')
            return redirect('accounts:warning-page')
    
    return wrapper


#allow customers to views their certificate applications and restrict the admin to do so.
def users_authentication(users_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_superuser:
            return users_func(request, *args, **kwargs)
        else:
            #return HttpResponse("You are not logged in, Log in to view this page.")
            return redirect('accounts:warning-page')
    
    return wrapper




def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper(request, *args, **kwargs):

            group = None 
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
            else:
                return redirect('accounts:warning-page')

        return wrapper
    return decorators
