from flask import Flask, render_template, request

app = Flask(__name__)

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

@app.route('/', methods=['GET', 'POST'])
def temperature_converter():
    if request.method == 'POST':
        temperature = float(request.form['temperature'])
        unit = request.form['unit']

        if unit == 'celsius':
            result = fahrenheit_to_celsius(temperature)
        else:
            result = celsius_to_fahrenheit(temperature)

        return render_template('index.html', result=result, unit=unit)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
