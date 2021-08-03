import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from preprocessing.cleaning_data import preprocess
from model.get_model import get_model

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def index():
    return "I'm alive, you can go to /predict"

@app.route('/predict', methods = ['GET', 'POST'])
def make_prediction():
    if request.method == 'GET':
        return "make POST request instead"
    else:
        input = request.json
        processed_input = preprocess(input)
        prediction = model.predict(processed_input)
        return jsonify({"price": list(prediction)[0]})

if __name__ == '__main__':
    model = get_model()
    port = int(os.environ.get('PORT', 5000))
    # Threaded option to enable multiple instances for
    # multiple user access support
    # You will also define the host to "0.0.0.0" because localhost will only be reachable from inside de server.
    app.run(host="0.0.0.0", threaded=True, port=port)
