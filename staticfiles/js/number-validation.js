const numberInput = document.getElementById('numberInput');
console.log('Number Validation is running')
// Optional: Add validation to only allow numbers
numberInput.addEventListener('input', function() {
    this.value = this.value.replace(/[^0-9]/g, ''); // Remove non-numeric characters
});