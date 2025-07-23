from unittest import result
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        size = float(request.form['size'])
        location = request.form['location']
        type = request.form['type']
        
        # Basic price calculation (example rates in PKR per square foot)
        base_price_per_sqft = {
            'gulberg': 22000,
            'dha': 25000,
            'johartown': 15000,
            'modeltown': 21667,  # New: Added for Model Town**
            'faisaltown': 17000,  # New: Added for Faisal Town**
            'defenceresidency': 22000,  # New: Added for Defence Residency
            'midcity': 5778,  # New: Added for Midcity Housing
            'bahriatown':16000
        }
        type_multiplier = {
            'house': 1.3,
            'apartment': 1.0,
            'plot': 0.8
        }
        if size<=0:
            return render_template('index.html', result="Size must be greater than 0.")         
        price = size * base_price_per_sqft[location] * type_multiplier[type]
        price = round(price, 2)
        
        return render_template('index.html', result=f"{price:,.2f}",location=location.capitalize())  # Updated: Formatted with 2 decimal places for clarity
    except ValueError:
        return render_template('index.html', result="Error in calculation. Please check your input.")

if __name__ == '__main__':
    app.run(debug=True)
