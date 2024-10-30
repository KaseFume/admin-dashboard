function exportData() {
            // Implement export functionality here
            alert("Data exported successfully!");
        }

        function saveData() {
            // Implement save functionality here
            alert("Data saved locally!");
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
            // Implement add new user functionality here
            alert("Add New User functionality to be implemented.");
        }

        function editUser(username) {
            // Implement edit user functionality here
            alert("Edit user: " + username);
        }

        function deleteUser(username) {
            // Implement delete user functionality here
            alert("Delete user: " + username);
        }