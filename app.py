from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        weight = float(request.form['weight'])  # Weight in kg
        feet = int(request.form['feet'])       # Height in feet
        inches = int(request.form['inches'])   # Additional height in inches
        
        # Convert height to meters
        height_m = ((feet * 12) + inches) * 0.0254
        
        # Calculate BMI
        bmi = round(weight / (height_m ** 2), 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        return render_template('result.html', bmi=bmi, category=category)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
