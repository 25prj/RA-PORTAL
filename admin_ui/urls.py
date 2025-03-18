from django.urls import path 

from . import views 

#app_name = 'admin_ui'

urlpatterns =[
    path('admin_ui/',views.admin_ui,name='admin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('type-approvals/',views.type_approval,name='type-approval'),
    path('approval-details/<int:view_id>',views.details,name='details')
    
]