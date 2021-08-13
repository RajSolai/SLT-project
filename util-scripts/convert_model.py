import tensorflow as tf

saved_model = '/home/solairaj/office/SLT-project/models/keras_model.h5'

save_tflite_model = '/home/solairaj/office/SLT-project/models/model.tflite'

model = tf.keras.models.load_model(saved_model)

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model.
with open(save_tflite_model, 'wb') as f:
  f.write(tflite_model)
