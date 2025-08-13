from django.contrib.auth.models import User
from accounts.models import DealershipLicense,TypeApproval
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.core.mail import send_mail
from django.dispatch import receiver
from accounts.utils import send_otp
from django.conf import settings


#signal to send user an email after the type approval applicatioin has responded to by admin
@receiver(post_save, sender=TypeApproval, dispatch_uid='typeapproval_status_response')
def typeapproval_status_response(sender,instance, **kwargs):
    if instance.status:
        subject = f'Your Type Approval Certificate is {instance.status}'

        if instance.status.lower() == 'approved':
            body=f'''
                Dear {instance.contact_person},

                We are pleased to inform you that your Type Approval Certificate application for {instance.product_type} has been APPROVED.

                Next Steps:
                - Download your certificate from the NCA Portal: [Link].
                - Contact support@nca.gov for inquiries.

                Best regards,
                NCA Team
            '''
        elif instance.status.lower() == 'under review':
            body= f'''
                Dear {instance.contact_person},

                
                Your application for {instance.product_type}  is UNDER REVIEW. Expect updates within 5 business days.
                
                Best regards,
                NCA Team

            '''      
        elif instance.status.lower() == 'rejected':
            body= f'''
                Dear {instance.contact_person},
        
                Your application for {instance.product_type}  was REJECTED due to:
                <404: under development>.
                
                Resubmit after corrections via [Portal Link].
                
                Best regards,
                NCA Team

            '''
        else:
            body=f'''
                Dear {instance.contact_perosn},
                We have successfully received your application for a Type Approval Certificate for {instance.product_type}.  

                \n**What Happens Next?**  
                \t- Your application will undergo a review process.  
                \t- You will be notified via email once a decision is made.  
                
                \n**Important Notes:**  
                \t- Ensure your contact information is up-to-date in the NCA Portal.  
                \t- Track your application status anytime at: [Portal Login Link].

                \nThank you for choosing NCA Certification Services.

            '''

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=False,
        )


#signal to send email to user after the dealership license has been responded to by the admin
@receiver(post_save,sender=DealershipLicense,dispatch_uid="dealership_status_response")
def dealership_status_response(sender, instance, **kwargs):
    if instance.status:
        print('status responsed ', instance.status)

        

        send_mail(
            f'Your Type Approval Certificate is {instance.status}',
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
            'Thanks for signing up',
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=False,
        )
