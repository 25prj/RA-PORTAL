from django.contrib.auth.models import User
from accounts.models import DealershipLicense,TypeApproval
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.core.mail import send_mail
from django.dispatch import receiver
from accounts.utils import send_otp


#signal to send user an email after the type approval applicatioin has responded to by admin
@receiver(post_save, sender=TypeApproval, dispatch_uid='typeapproval_status_response')
def typeapproval_status_response(sender,instance, **kwargs):
    if instance.status:
        send_mail(
            'Type Approval Application Notifications',
            f'your type approval of {instance.company_name} is {instance.status}',
            'admin@django.com',
            [instance.email],
            fail_silently=False,
        )

#signal to send email to user after the dealership license has been responded to by the admin
@receiver(post_save,sender=DealershipLicense,dispatch_uid="dealership_status_response")
def dealership_status_response(sender, instance, **kwargs):
    if instance.status:
        print('status responsed ', instance.status)

        send_mail(
            'Dealership LIcense Notificatioin',
            f'your dealership license application has {instance.status}',
            'admin@django.com',
            [instance.email],
            fail_silently=False,
        )
        

#sending user a welcome message after signing up 
@receiver(post_save,sender=User, dispatch_uid="send_welcome_email")
def send_welcome_email(sender,instance,created,**kwargs):
    """ send a welcome message"""
    
    print('signal fired...')
    if created:
        send_mail(
            'Welcome !',
            'Thanks for signing',
            'admin@django.com',
            [instance.email],
            fail_silently=False,
        )
