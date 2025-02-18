from django.urls import path 

from . import views

app_name = 'user_ui'

urlpatterns =[
       
    path("type-approval/",views.type_approval_view, name="type-approval"),
    path("success-page/",views.success_page, name="success-page"),
    path("type-approval-list/",views.type_approval_list, name='type-approval-list'),
    path("approval-view/<int:view_id>/", views.approval_view, name="approval-view"),
]
