from django.urls import path 

from . import views 

#app_name = 'admin_ui'

urlpatterns =[
    path('admin_ui/',views.admin_ui,name='admin'),
    path('dashboard/', views.dashboard, name='dashboard'),
]