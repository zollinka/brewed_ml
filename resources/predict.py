from flask_restful import Resource, reqparse

class Predict(Resource):
	def __init__(self):
		super().__init__()
		self.parser = reqparse.RequestParser()
		self.parser.add_argument('image_path', required=True)
	
	def post(self):
		img_path = self.parser.parse_args().image_path
		return {'result':img_path}
