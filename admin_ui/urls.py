from django.urls import path 

from . import views 

#app_name = 'admin_ui'

urlpatterns =[
    path('admin_ui/',views.admin_ui,name='admin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('type-approvals/',views.type_approval,name='type-approval'),
    path('approval-details/<int:view_id>',views.details,name='details'),
    path('typeappoval-list', views.type_approval_textFile, name='approval-text'),
    path('delete-approval/<int:pk>/',views.delete_approval, name='delete-approval'),

    path('admin-dealership-license-list/', views.dealership_license_list, name='dealership_list'),
    path('dealership-view-details/<int:view_id>/', views.dealership_view_details, name='dealership-details'),
    path('delete-dealership-license/<int:pk>/',views.delete_dealership_license, name='delete-dealership'),

    path('users-list/', views.users_list, name='users-list'),
    path('adding-user/',views.creating_user, name='add-user'),
    path('delete-user/<int:pk>/', views.delete_user, name='delete-user'),
    
]