from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func


def admin_only(admin_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return admin_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized to view this page')
    
    return wrapper

#check if user is logged in else redirect user to a "not authorized page."
def user_authentication(user_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return user_func(request, *args, **kwargs)
        else:
            return HttpResponse('you are not logged in')
        

    return wrapper