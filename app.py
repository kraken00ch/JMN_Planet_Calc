# app.py (Flask backend)
from flask import Flask, render_template, request, jsonify
from user_input import get_user_weight, get_planet_selection
from planet_calculation import calculate_weight_on_planet
from display_info import display_weight_info

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()  # Extract JSON data from the request body
        userweight = data.get('userweight')
        planet = int(data.get('planet'))

        # Perform calculations based on user input
        result = calculate_weight_on_planet(userweight, planet)

        if result is not None:
            # Return a JSON response with calculated values
            return jsonify({'earthweight': userweight, 'planetweight': result})
        else:
            # Return an error response with an appropriate status code
            return jsonify({'error': 'Calculation failed'}), 500
    except ValueError:
        # Return an error response for invalid input
        return jsonify({'error': 'Invalid input. Please enter valid numbers.'}), 400

if __name__ == '__main__':
    app.run()
