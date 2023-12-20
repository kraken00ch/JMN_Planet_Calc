from flask import Flask, render_template, request
from JMN_Planet_Calc import get_user_weight, get_planet_selection, calculate_weight_on_planet

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    userweight = get_user_weight()
    planet = get_planet_selection()
    result = calculate_weight_on_planet(userweight, planet)
    return render_template('result.html', userweight=userweight, result=result)

if __name__ == '__main__':
    app.run(debug=True)