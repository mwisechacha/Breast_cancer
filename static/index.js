let display = false;

document.addEventListener('DOMContentLoaded', function () {
    var resultElement = document.getElementById('result');
    var submitButton = document.getElementsByClassName('submit-button');
    var predictionForm = document.getElementById('predictionForm');

    // Add event listener to the form submit event
    predictionForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting and refreshing the page
        
        display = true;
        console.log('Form was submitted!');

        // Update resultElement when form is submitted
        resultElement.textContent = "Result";
        resultElement.classList.remove('hidden');
    });

    // Check display when DOM is loaded (though it's redundant in this simplified case)
    if (display) {
        resultElement.textContent = "Result";
        resultElement.classList.remove('hidden');
    }
});
