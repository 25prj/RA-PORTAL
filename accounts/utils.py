import pyotp 
from datetime import datetime,timedelta
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

'''
email_list = []
for user in User.objects.all():
    email_list.append(user.email)
'''

def send_otp(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return False
    
    totp = pyotp.TOTP(pyotp.random_base32(), interval=120)
    otp = totp.now()
    request.session['otp_secret_key'] = totp.secret
    valid_date = datetime.now() + timedelta(minutes = 1)
    request.session['otp_valid_date'] = str(valid_date)

    print(f'\nYour otp: {otp}')

    subject = "Your one-time password"
    message = f'''
    Hello {user.username},

    Your OTP for login is: {otp}
    This code is valid for 1 minute.

    If you didn't request this, please ignore this email.
'''

    send_mail(
        subject=subject,
        message=message,
        from_email='admin@django.com',
        recipient_list=[user.email],
        fail_silently=False,
        )
        
     

    

   


    
'''
def countdown(valid_date):
    while datetime.now() < valid_date:
        remaining = valid_date - datetime.now()
        seconds = remaining.total_seconds()
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(int(mins), int(secs))
        print(f"Time remaining: {timer}", end="\r")
        time.sleep(1)
    print("\nOTP has expired!")
'''