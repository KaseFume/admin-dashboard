import random
from django.core.mail import send_mail
from .models import OTP

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(user):
    otp_code = generate_otp()
    OTP.objects.update_or_create(user=user, defaults={'otp_code': otp_code})

    send_mail(
        'Your OTP Code',
        f'Your OTP code is {otp_code}',
        'your-email@gmail.com',  # From email
        [user.email],  # To email
        fail_silently=False,
    )
