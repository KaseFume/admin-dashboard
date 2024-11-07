function exportData() {
            // Implement export functionality here
            window.location.href = "../export-data/";
        }

        function saveData() {
            // Implement save functionality here
            window.location.href = "../save-local/";
        }

        function toggleContactDetails() {
            const details = document.getElementById('contact-details');
            details.style.display = (details.style.display === "none" || details.style.display === "") 
                ? "block" 
                : "none";
        }
        
        function toggleUserManagementDetails() {
            const details = document.getElementById('user-management-details');
            details.style.display = (details.style.display === "none" || details.style.display === "") 
                ? "block" 
                : "none";
        }
        

        function togglePassword(passwordId) {
            const passwordField = document.getElementById(passwordId);
            const isHidden = passwordField.style.display === "none";
            passwordField.style.display = isHidden ? "inline" : "none"; // Toggle visibility
        }
        function addNewUser() {
            const email = prompt("Enter email:");
            const password = prompt("Enter password:");
        
            fetch("../../dashboard/add-user/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ email, password })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => alert(data.message))
            .catch(error => alert('Error: ' + error.message));
        }
        
        function editUser(email) {
            const newEmail = prompt("Enter new email for " + email + ":");
        
            fetch("{% url 'data:edit_user' email=email %}", { // Updated to correctly format the URL
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ email: newEmail })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => alert(data.message))
            .catch(error => alert('Error: ' + error.message));
        }
        
        function deleteUser(email) {
            if (confirm(`Are you sure you want to delete user ${email}?`)) {
                fetch("{% url 'data:delete_user' email=email %}", { // Updated to correctly format the URL
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken')
                    }
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => alert(data.message))
                .catch(error => alert('Error: ' + error.message));
            }
        }
        
        // Helper function to get CSRF token
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Check if this cookie string begins with the name we want
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
            