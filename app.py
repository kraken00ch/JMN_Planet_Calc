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
        data = request.get_json()
        userweight = data.get('userweight')
        planet = int(data.get('planet'))

        # Perform calculations based on user input
        result = calculate_weight_on_planet(userweight, planet)

        if result is not None:
            return jsonify({'earthweight': userweight, 'planetweight': result})
        else:
            return jsonify({'error': 'Calculation failed'}), 500

    except ValueError as ve:
        app.logger.error(f"ValueError: {ve}")
        return jsonify({'error': 'Invalid input. Please enter valid numbers.'}), 400

    except Exception as e:
        app.logger.error(f"Internal Server Error: {e}", exc_info=True)  # Log the exception traceback
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run()
