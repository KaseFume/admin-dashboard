const loginForm = document.getElementById('login-form');
const otpForm = document.getElementById('otp-form');
const loadingIndicator = document.getElementById('loading-indicator');
const resendOtp = document.getElementById('resend-otp');
const backToLoginBtn = document.getElementById('back-to-login-btn');

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
    showLoading();  // Show loading indicator when form is submitted
});

// Handle form submission for the OTP form
otpForm.addEventListener('submit', (e) => {
    showLoading();  // Show loading indicator when OTP form is submitted
});

// Handle Back to Login button
backToLoginBtn.addEventListener('click', () => {
    otpForm.classList.add('hidden');  // Hide OTP form
    loginForm.classList.remove('hidden');  // Show login form
});

// Handle OTP resend
resendOtp.addEventListener('click', () => {
    showLoading();  // Show loading indicator
    fetch("{% url 'resend_otp' %}", {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',  // Include CSRF token
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})  // Send an empty body for the request
    })
    .then(response => {
        hideLoading();  // Hide loading indicator after receiving response
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();  // Parse JSON from response
    })
    .then(data => {
        alert(data.message);  // Show success message from server response
    })
    .catch(error => {
        hideLoading();  // Hide loading indicator
        alert('An error occurred: ' + error.message);  // Show error message
    });
});
