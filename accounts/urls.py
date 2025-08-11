from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('signup/',views.signup, name='signup'),
    path('logout/',views.logout_user,name="logout"),
    path('warning-page/',views.warning_page, name='warning-page'),
    path('otp-page/',views.otp_view,name='otp-page'),
    #path('password-reset/',views.password_change, name='password-change'),
    

    path('reset_password/',auth_views.PasswordResetView.as_view(), name="reset_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name="password_rest_comfirm"),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),  name="password_reset_complete",),

]
