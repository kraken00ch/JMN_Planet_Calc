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
