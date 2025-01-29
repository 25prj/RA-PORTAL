from django.urls import path 

from . import views

app_name = "user_ui"

urlpatterns =[
    path("type-approval/", views.TypeApproval_page, name="type-approval")
]
