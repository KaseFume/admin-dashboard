const loginForm = document.getElementById('login-form');
const otpForm = document.getElementById('otp-form');
const loadingIndicator = document.getElementById('loading-indicator');
const resendOtpBtn = document.getElementById('resend-btn');
const backToLoginBtn = document.getElementById('back-to-login-btn');
const resendMessage = document.getElementById('resend-message');

// CSRF token from the template
const csrfToken = "{{ csrf_token }}";

// Show loading indicator
function showLoading() {
    loadingIndicator.classList.remove('hidden');
}

// Hide loading indicator
function hideLoading() {
    loadingIndicator.classList.add('hidden');
}

// Handle form submission for the login form
loginForm.addEventListener('submit', (e) => {
    e.preventDefault();  // Prevent page reload
    showLoading();  // Show loading indicator
    loginForm.submit();  // Submit the form manually after showing the loading indicator
});

// Handle form submission for the OTP form
otpForm.addEventListener('submit', (e) => {
    e.preventDefault();  // Prevent page reload
    showLoading();  // Show loading indicator
    otpForm.submit();  // Submit the form manually after showing the loading indicator
});

// Handle Back to Login button
backToLoginBtn.addEventListener('click', () => {
    otpForm.classList.add('hidden');  // Hide OTP form
    loginForm.classList.remove('hidden');  // Show login form
});

// Handle OTP resend
