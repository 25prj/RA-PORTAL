from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


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
            #return HttpResponse('You are not authorized to view this page')
            return redirect('accounts:warning-page')
    
    return wrapper


def users_authentication(users_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_superuser:
            return users_func(request, *args, **kwargs)
        else:
            #return HttpResponse("You are not logged in, Log in to view this page.")
            return redirect('accounts:warning-page')
    
    return wrapper