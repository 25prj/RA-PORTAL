from django.urls import path 

from . import views
urlpatterns =[
       
    path("type-approval/",views.type_approval, name="type-approval"),
]
