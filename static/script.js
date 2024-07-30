// static/script.js

function predict() {
    const self_study = document.getElementById('self_study').value;
    const tutorials = document.getElementById('tutorials').value;

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `self_study=${self_study}&tutorials=${tutorials}`
    })
    .then(response => response.json())
    .then(data => {
        displayProbability(data.result);
    })
    .catch(error => {
        console.error('Error:', error);
    });
} 

function displayProbability(probability) {
    const predictionResultDiv = document.getElementById('predictionResult');
    predictionResultDiv.innerHTML = `<p>Probability of passing: ${probability.toFixed(2)}%</p>`;
    
    // Show prediction result
    predictionResultDiv.style.display = 'block';
}
