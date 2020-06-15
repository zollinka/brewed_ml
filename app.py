#!flask/bin/python
from flask import Flask
from flask_restful import Api
from resources.predict import Predict

app = Flask(__name__)
api = Api(app)

api.add_resource(Predict, '/api/predict')

if __name__ == '__main__':
	app.run(debug=True)
