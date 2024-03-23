from flask import Flask, jsonify, send_file
import matplotlib.pyplot as plt
import io
import json
from flask_cors import CORS
from graph import net_predicted_sectors, emissions_per_sector
from backend import func

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    data_array = func()
    
    if not data_array or not isinstance(data_array[0], list) or len(data_array[0]) < 3:
        return jsonify({"error": "Invalid data format"}), 400
    
    sample_row = data_array[0]
    
    data = {
        'company': sample_row[0],
        'sector': sample_row[1],
        'cost': sample_row[2]
    }
    
    return jsonify(data)


@app.route('/plot')
def plot():
    return net_predicted_sectors()

if __name__ == '__main__':
    app.run(debug=True)
