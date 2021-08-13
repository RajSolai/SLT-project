import cv2
import tensorflow.keras
import numpy as np

class app:
	# constructor
	def __init__(self):
		super(app, self).__init__()
		capture = cv2.VideoCapture(0)
		frameWidth = 1280
		frameHeight = 720
		# set width and height in pixels
		capture.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth)
		capture.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHeight)
		# enable auto gain
		capture.set(cv2.CAP_PROP_GAIN, 0)
		# Disable scientific notation for clarity
		np.set_printoptions(suppress=True)
		# Load the model
		model = tensorflow.keras.models.load_model('keras_model.h5')
		while True:
			# shape = (no.of images , (our image shape))
			data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

			check, frame = capture.read()
			
			margin = int(((frameWidth-frameHeight)/2))
			square_frame = frame[0:frameHeight, margin:margin + frameHeight]
			
			resized_img = cv2.resize(square_frame, (224, 224))
		
			model_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)

			#turn the image into a numpy array
			image_array = np.asarray(model_img)

			# Normalize the image
			normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

			# Load the image into the array
			data[0] = normalized_image_array

			# run the inference
			prediction = model.predict(data)
			

		"""end of main engine"""

# main function
if(__name__=="__main__"):
	_app = app()