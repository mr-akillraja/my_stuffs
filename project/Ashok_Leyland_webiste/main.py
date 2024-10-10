from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
@app.route('/search', methods=['POST'])
def search():
    input_id = request.form.get('asset_id')
    input_serial = request.form.get('serial_number')

    data = pd.read_csv("input.csv")

    if input_id:
        asset_id = data[data['ASSET ID'] == input_id]
        serial = pd.DataFrame()
    elif input_serial:
        asset_id = pd.DataFrame()
        serial = data[data['SERIAL NUM'] == input_serial]
    else:
        asset_id = pd.DataFrame()
        serial = pd.DataFrame()

    return render_template('result.html', asset_id=asset_id, serial=serial)


if __name__ == '__main__':
    app.run(debug=True)
