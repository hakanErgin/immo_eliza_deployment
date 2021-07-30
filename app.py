# app.py
import os
from flask import Flask, request, jsonify
from preprocessing.cleaning_data import preprocess

app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Alive, go to predict</h1>"

@app.route('/predict', methods = ['GET', 'POST'])
def make_prediction():
    if request.method == 'GET':
        return "<h1>make POST request instead</h1>"
    else:
        json = request.get_json()
        
        return preprocess(json)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Threaded option to enable multiple instances for
    # multiple user access support
    # You will also define the host to "0.0.0.0" because localhost will only be reachable from inside de server.
    app.run(host="0.0.0.0", threaded=True, port=port)
