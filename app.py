# app.py (Flask backend)
from flask import Flask, render_template, request, jsonify
from JMN_Planet_Calc.py import calculate_weight_on_planet

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    userweight = float(request.form['userweight'])
    planet = int(request.form['planet'])
    result = calculate_weight_on_planet(userweight, planet)
    return jsonify({'userweight': userweight, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)
