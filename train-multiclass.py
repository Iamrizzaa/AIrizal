
import sys
import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K

train_data_dir = './data/train'
validation_data_dir = './data/validation'

"""
Parameters
"""
img_width, img_height = 150, 150
nb_train_samples = 150
nb_validation_samples = 100
epochs = 10
batch_size = 64

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)


model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))


model.add(Flatten())
model.add(Dense(150))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(36, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical')


hist = model.fit_generator(
    train_generator,
    steps_per_epoch = nb_train_samples // batch_size,
    epochs=epochs,
    validation_data = validation_generator,
    validation_steps = nb_validation_samples // batch_size)

target_dir = './models/'
if not os.path.exists(target_dir):
  os.mkdir(target_dir)
model.save('./models/model.h5')
model.save_weights('./models/weights.h5')


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


plt.plot (hist.history['loss'], color = 'blue', label = 'train')
plt.plot (hist.history['val_loss'], color = 'orange', label = 'train')
plt.grid(True)
plt.title("Train & test loss with epochs\n", fontsize = 16)
plt.xlabel ("Training epochs", fontsize=12)
plt.ylabel ("Train & test loss", fontsize=12)
plt.show()

plt.plot (hist.history['acc'], color = 'blue', label = 'train')
plt.plot (hist.history['val_acc'], color = 'orange', label = 'train')
plt.grid(True)
plt.title("Train & test accuracy with epochs\n", fontsize=16)
plt.xlabel ("Training epochs", fontsize=12)
plt.ylabel ("Train & test loss", fontsize=12)
plt.show()

