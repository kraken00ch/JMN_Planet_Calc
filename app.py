# app.py (Flask backend)
from flask import Flask, render_template, request, jsonify
from gravity_calculator_app import calculate_weight_for_user_on_planet

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()  # Extract JSON data from the request body
        userweight, result = calculate_weight_for_user_on_planet()

        return jsonify({'earthweight': userweight, 'planetweight': result})
    except ValueError as e:
        # Return an error response for invalid input
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # Return an error response for other exceptions
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
