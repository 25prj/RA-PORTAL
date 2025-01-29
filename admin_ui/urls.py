from django.urls import path 

from . import views 

urlpatterns =[
    path('admin_ui/',views.admin_ui,name='admin_ui'),
]