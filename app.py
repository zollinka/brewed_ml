#!flask/bin/python
from flask import Flask
from flask_restful import Api
from resources.predict import Predict
from tensorflow.keras.models import load_model

MODEL_PATH = 'MobileNet_F_20'

app = Flask(__name__)
api = Api(app)
model = load_model(MODEL_PATH)

api.add_resource(Predict, '/api/predict', resource_class_kwargs = {'model':model})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
