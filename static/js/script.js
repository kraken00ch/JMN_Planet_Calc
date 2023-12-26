// static/js/script.js

function calculateWeight() {
    const userweight = document.getElementById('userweight').value;
    const planet = document.getElementById('planet').value;

    // Make an asynchronous request to the Flask backend
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `userweight=${userweight}&planet=${planet}`,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Calculation failed');
        }
        return response.json();
    })
    .then(data => {
        // Update the GUI with the calculation result
        document.getElementById('earthWeight').innerText = `Weight on Earth: ${data.userweight} lbs`;
        document.getElementById('planetWeight').innerText = `Weight on selected planet: ${data.result} lbs`;

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

    // Delay the form submission to retain the input box value
    setTimeout(function () {
        // Call the calculateWeight function
        calculateWeight();
    }, 0);
});

// Add an event listener to the userweight input for keyup events
document.getElementById('userweight').addEventListener('keydown', function (event) {
    // Check if the key pressed is Enter (key code 13)
    if (event.key === 'Enter' || event.keyCode === 13) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Delay the form submission to retain the input box value
        setTimeout(function () {
            // Call the calculateWeight function
            calculateWeight();
        }, 0);
    }
});
