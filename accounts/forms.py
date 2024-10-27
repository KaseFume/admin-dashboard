from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()

class OTPForm(forms.Form):
    otp_code = forms.CharField(max_length=6)
