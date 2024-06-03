let display = false;

document.addEventListener('DOMContentLoaded', function () {
    var resultElement = document.getElementById('result');
    var submitButton = document.getElementsByClassName('submit-button');
    var predictionForm = document.getElementById('predictionForm');


    predictionForm.addEventListener('submit', function(event) {
        event.preventDefault(); 
        
        display = true;
        console.log('Form was submitted!');


        resultElement.textContent = "Result";
        resultElement.classList.remove('hidden');
    });


    if (display) {
        resultElement.textContent = "Result";
        resultElement.classList.remove('hidden');
    }
});
