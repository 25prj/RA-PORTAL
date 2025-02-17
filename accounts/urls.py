from django.urls import path 
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('signup/',views.signup, name='signup'),
    path('logout/',views.logout_user,name="logout"),
    path('warning-page/',views.warning_page, name='warning-page')
]
