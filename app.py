from flask import Flask
import threading
import time

from flask import Flask , request, jsonify
from time import sleep
from flask_cors import CORS
import read_data
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return jsonify('Welcome to stock api')

@app.route('/api/stock/all', methods=['GET'])
def api_stockall():
    data = read_data.read('stocks')
    return jsonify(data)  # Assuming this code is part of a Flask web application
 
@app.route('/api/stock/get_top10_gainer_data', methods=['GET'])
def api_get_top10_gainer_data():
    data = read_data.read('topgainer')
    return jsonify(data)  # Assuming this code is part of a Flask web application
 
@app.route('/api/stock/get_top10_loser_data', methods=['GET'])
def api_get_top10_loser_data():
    data = read_data.read('toplooser')
    return jsonify(data)  # Assuming this code is part of a Flask web application
 
@app.route('/api/stock/get_top20_share_data', methods=['GET'])
def api_get_top20_share_data():
    data = read_data.read('top20stock')
    return jsonify(data)  # Assuming this code is part of a Flask web application
 
if __name__ == "__main__":
    app.run(use_reloader=False)
    