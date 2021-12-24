from __main__ import app
from flask import request, jsonify
from core.test_single import predictSign


@app.route('/foo', methods=['POST'])
def foo():
    data = request.json
    return jsonify(data)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    vId = data['vId']
    predict = predictSign([vId])

    response = {
        "vId": vId,
        "prediction": predict
    }
    return jsonify(response)
