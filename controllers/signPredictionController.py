from __main__ import app
from flask import request, jsonify


@app.route('/foo', methods=['POST'])
def foo():
    data = request.json
    return jsonify(data)
