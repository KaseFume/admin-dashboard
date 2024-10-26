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
document.getElementById("resend-otp").addEventListener("click", function () {
    log.console('You just interact bullsht')
    fetch("{% url 'resend_otp' %}", {
      method: "POST",
      headers: {
        "X-CSRFToken": "{{ csrf_token }}", // CSRF token is necessary for security
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ action: "resend" }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          document.getElementById("resend-message").classList.remove("hidden");
          document.getElementById("resend-message").innerText = "OTP has been resent!";
        } else {
          alert("Failed to resend OTP. Please try again.");
        }
      })
      .catch((error) => console.error("Error:", error));
  });
  
