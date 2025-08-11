from django.urls import path 
from django.conf.urls.static import static
from django.conf import settings



from . import views
from .views import TypeApprovalView,dealershipView

app_name = 'user_ui'

urlpatterns =[

    #path('type-approval-form-wizard/', views.TypeApprovalWizardView.as_view()),
    path('type-approval-form/', TypeApprovalView.as_view(), name='type_approval_form'),
    #path("type-approval/",views.type_approval_view, name="type-approval"),


    path("success-page/",views.success_page, name="success-page"),
    path("type-approval-list/",views.type_approval_list, name='type-approval-list'),
    path("approval-view/<int:approval_id>/", views.approval_view, name="approval-view"),
    path('approval-edit/<int:approval_id>/', views.approval_edit, name='approval-edit'),
    
    path("dealership-license/", views.dealership, name='dealership'),
    path("dealership-form/",dealershipView.as_view(), name='dealershipForm'),
    path("dealership-license-list/",views.dealership_license_list, name='dealership-list'),
    path('dealership-license-view/<int:pk>/',views.dealership_license_view, name='dealership-view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
