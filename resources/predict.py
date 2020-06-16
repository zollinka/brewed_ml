from flask_restful import Resource, reqparse
import numpy as np
from PIL import Image,ImageOps
import keras

class Predict(Resource):
	def __init__(self, **kwargs):
		super().__init__()
		self.model = kwargs['model']
		self.parser = reqparse.RequestParser()
		self.parser.add_argument('image_path', required=True)
	
	def post(self):
		img_path = self.parser.parse_args().image_path
		self.convert_image(img_path)
		input_arr = self.get_image_from_path(img_path)
		prediction = self.model.predict(input_arr)
		class_p = prediction.argmax(axis=-1)
		lab_csv = np.loadtxt('labels_v1.csv', dtype=[('EAN','U13'),('Name','S')],delimiter=';',encoding='latin-1')
		labels = lab_csv['EAN']
		result_label = labels[class_p + 1]
		return {'result':result_label[0]}

	def __get_image_from_path(self, img_path):
		image = keras.preprocessing.image.load_img(img_path, target_size=(224,224))
		input_arr = keras.preprocessing.image.img_to_array(image)
		input_arr /= 255
		input_arr = np.array([input_arr])
		return input_arr

	def __exif_transpose(self, img):
		if not img:
			return img
		exif_orientation_tag = 274
		if hasattr(img, "_getexif") and isinstance(img._getexif(), dict) and exif_orientation_tag in img._getexif():
			exif_data = img._getexif()
			orientation = exif_data[exif_orientation_tag]
			if orientation == 1 or orientation == 2 or orientation == 4 or orientation == 5 or orientation == 7:
				pass
			elif orientation == 3:
				img = img.rotate(180)
			elif orientation == 6:
				img = img.rotate(-90, expand=True)
			elif orientation == 8:
				img = img.rotate(90, expand=True)

	def __convert_image(self,path,mode='RGB'):
		img = Image.open(path)
		if hasattr(ImageOps, 'exif_transpose'):
			img = ImageOps.exif_transpose(img)
		else:
			img = exif_transpose(img)
		img = img.convert(mode)
		img.save(path)
		return 0


	def __save_image_from_request(self):
		return 'lala'
