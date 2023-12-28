// script.js
function calculateWeight() {
    const userweight = document.getElementById('userweight').value;
    const planet = document.getElementById('planet').value;

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ userweight, planet }),
    })
    .then(response => {
        if (!response.ok) {
            return response.text().then(errorMessage => {
                console.error('Server Error:', errorMessage);
                throw new Error('Calculation failed');
            });
        }
        return response.json();
    })
    .then(data => {
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
