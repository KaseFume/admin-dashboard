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

        # Check if OTP is valid
        if email in otp_storage and str(otp_storage[email]) == entered_otp:
            user = authenticate(request, email=email)
            if user:
                login(request, user)  # Log the user in
                otp_storage.pop(email)  # Remove OTP from storage
                return HttpResponse('Logged in successfully!')

        # Render with error message for invalid OTP
        return render(request, 'accounts/2fa.html', {'error_message': 'Incorrect OTP.', 'otp_sent': True})

    return redirect('send_otp')



def resend_otp(request):
    if request.method == 'POST':
        email = request.session.get('user_email')
        if email in otp_storage:
            otp = random.randint(100000, 999999)
            otp_storage[email] = otp  # Save new OTP in memory

            # Send the new OTP via email
            send_mail(
                'Your OTP Code',
                f'Your new OTP is {otp}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return JsonResponse({'message': 'OTP resent successfully!'})
        return JsonResponse({'error': 'Email not found.'}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

