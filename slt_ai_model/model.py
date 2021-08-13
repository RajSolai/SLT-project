import tensorflow as tf
import numpy as np

#params
image_size = (180,180)
batch_size = 5
train_epochs = 0

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "/home/solairaj/office/SLT-project/train_data_set",
    validation_split=0,
    seed=None,
    color_mode='rgb',
    image_size=image_size,
    batch_size=batch_size,
)

validation_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "/home/solairaj/office/SLT-project/train_data_set",
    validation_split=0,
    seed=None,
    color_mode='rgb',
    image_size=image_size,
    batch_size=batch_size,
)

# build and train model
model = tf.keras.Sequential([
        #(input_shape=(180,180,3)),
        tf.keras.layers.Conv2D(32,3,padding='same',activation='relu',input_shape=(180,180,3)),
        tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
        tf.keras.layers.Conv2D(64,3,padding='same',activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(units=64,activation='relu'),
        tf.keras.layers.Dense(units=128,activation='relu'),
        tf.keras.layers.Dense(units=64,activation='relu'),
        tf.keras.layers.Dense(units=2,activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'],
            )

model.fit(train_ds,epochs=train_epochs,validation_data=validation_ds,verbose=1)