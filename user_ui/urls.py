from django.urls import path 

from . import views

app_name = 'user_ui'

urlpatterns =[
       
    path("type-approval/",views.type_approval_view, name="type-approval"),
    path("success-page/",views.success_page, name="success-page"),
]
