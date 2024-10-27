from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login
from .models import CustomUser, OTP
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import random
from django.conf import settings
from django.http import JsonResponse


otp_storage = {}

def send_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user:
            # Generate a random 6-digit OTP
            otp = random.randint(100000, 999999)
            otp_storage[email] = otp  # Save OTP in memory

            # Send OTP via email
            send_mail(
                'Your OTP Code',
                f'Your OTP is {otp}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            request.session['user_email'] = email  # Store email in session

            # Render with otp_sent context
            return render(request, 'accounts/2fa.html', {'otp_sent': True})

        # Render with error message for invalid credentials
        return render(request, 'accounts/2fa.html', {'error_message': 'Incorrect email or password.'})

    return render(request, 'accounts/2fa.html')

def verify_otp(request):
    if request.method == 'POST':
        email = request.session.get('user_email')
        entered_otp = request.POST.get('otp')

        if not email:
            # If email isn't in session, redirect to login
            return redirect('send_otp')

        # Check if the entered OTP matches the stored OTP
        if email in otp_storage and str(otp_storage[email]) == entered_otp:
            user = CustomUser.objects.filter(email=email).first()
            if user:
                login(request, user)  # Log the user in
                otp_storage.pop(email)  # Remove OTP from memory
                return HttpResponse('Logged in successfully!')
            else:
                return render(request, 'accounts/2fa.html', {
                    'error_message': 'User not found.', 'otp_sent': True
                })

        # OTP is invalid
        return render(request, 'accounts/2fa.html', {
            'error_message': 'Incorrect OTP.', 'otp_sent': True
        })

    return redirect('send_otp')



def resend_otp(request):
    if request.method == 'GET':
        email = request.session.get('user_email')

        if not email:
            # Render with an error message
            return render(request, 'accounts/2fa.html', {
                'error_message': 'Email not in session.', 'otp_sent': False
            })

        if email in otp_storage:
            # Generate and save a new OTP
            otp = random.randint(100000, 999999)
            otp_storage[email] = otp

            # Send the new OTP via email
            send_mail(
                'Your OTP Code',
                f'Your new OTP is {otp}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            # Render the 2fa template with a success message
            return render(request, 'accounts/2fa.html', {
                'otp_sent': True, 'success_message': 'A new OTP has been sent to your email.'
            })

        # Render with an error if OTP is not found
        return render(request, 'accounts/2fa.html', {
            'error_message': 'OTP not found.', 'otp_sent': False
        })

    # Render with an error for invalid request method
    return render(request, 'accounts/2fa.html', {
        'error_message': 'Invalid request method.', 'otp_sent': False
    })