# !pip install flask_restful
# !pip install flask_cors
# !pip install flask_ngrok


from flask import Flask, request, jsonify
from flask_restful import Resource, Api
# from flask.ext.cors import CORS, cross_origin
from flask_cors import CORS, cross_origin
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
cors = CORS(app)
api = Api(app)
run_with_ngrok(app)


from controllers import signPredictionController 

# @app.route('/foo', methods=['POST'])
# def foo():
#     data = request.json
#     return jsonify(data)


if __name__ == '__main__':
    app.run()
