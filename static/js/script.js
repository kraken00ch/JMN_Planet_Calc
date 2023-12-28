// static/js/script.js

function calculateWeight() {
    const userweight = document.getElementById('userweight').value;
    const planet = document.getElementById('planet').value;

    // Make an asynchronous request to the Flask backend
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ userweight, planet }),
    })
    .then(response => response.json())
    .then(data => {
        if ('error' in data) {
            throw new Error(data.error);
        }

        // Update the GUI with the calculation result
        document.getElementById('earthWeight').innerText = `Weight on Earth: ${data.earthweight} lbs`;
        document.getElementById('planetWeight').innerText = `Weight on selected planet: ${data.planetweight} lbs`;

        // Display the result section
        document.getElementById('result').style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
        // Display error message on the GUI
        document.getElementById('earthWeight').innerText = 'Calculation failed';
        document.getElementById('planetWeight').innerText = '';
        document.getElementById('result').style.display = 'block';
    });
}

// Add an event listener to the form for submit events
document.getElementById('calculationForm').addEventListener('submit', function (event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Call the calculateWeight function
    calculateWeight();
});

// Add an event listener to the userweight input for input events
document.getElementById('userweight').addEventListener('input', function (event) {
    // Call the calculateWeight function
    calculateWeight();
});

// Add an event listener to the userweight input for keyup events
document.getElementById('userweight').addEventListener('keyup', function (event) {
    // Check if the pressed key is "Enter"
    if (event.key === 'Enter') {
        // Call the calculateWeight function
        calculateWeight();
    }
});

// Add an event listener to the planet dropdown for change events
document.getElementById('planet').addEventListener('change', function () {
    // Call the calculateWeight function when the selected planet changes
    calculateWeight();
});
