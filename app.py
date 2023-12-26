# app.py (Flask backend)
from flask import Flask, render_template, request, jsonify
from JMN_Planet_Calc import calculate_weight_on_planet

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        userweight = float(request.form['userweight'])
        planet = int(request.form['planet'])
        result = calculate_weight_on_planet(userweight, planet)

        if result is not None:
            # Return a JSON response with calculated values
            return jsonify({'userweight': userweight, 'result': result})
        else:
            # Return an error response with appropriate status code
            return jsonify({'error': 'Calculation failed'}), 500
    except ValueError:
        # Return an error response for invalid input
        return jsonify({'error': 'Invalid input. Please enter valid numbers.'}), 400

if __name__ == '__main__':
    app.run()