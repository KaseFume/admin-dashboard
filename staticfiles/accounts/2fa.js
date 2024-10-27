const loginForm = document.getElementById('login-form');
const otpForm = document.getElementById('otp-form');
const loadingIndicator = document.getElementById('loading-indicator');
const resendOtp = document.getElementById('resend-otp');
const backToLoginBtn = document.getElementById('back-to-login-btn');

// Toggle between forms based on OTP status
if (document.querySelector('[otp_sent]')) {
    loginForm.classList.add('hidden');
    otpForm.classList.remove('hidden');
}

// Show loading indicator
function showLoading() {
    loadingIndicator.classList.remove('hidden');
}

// Hide loading indicator
function hideLoading() {
    loadingIndicator.classList.add('hidden');
}

// Handle Back to Login button
backToLoginBtn.addEventListener('click', () => {
    otpForm.classList.add('hidden');
    loginForm.classList.remove('hidden');
});

// Handle OTP resend
resendOtp.addEventListener('click', () => {
    alert('OTP resent! Please check your email.');
});
