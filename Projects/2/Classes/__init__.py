############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    COVID-19 AI Classification
# Project:       COVID-19 Pneumonia Detection/Early Detection
#
# Author:        Aniruddh Sharma
# Title:         COVID-19 CT Scan Classification with Tensorflow
# Description:   Training Model with tensorflow by CT Scan Dataset for detecting Signs of COVID-19 in Patients
# License:       MIT License
# Last Modified: 2020-06-09
#
############################################################################################


import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Activation, Dropout, Flatten
from tensorflow.keras.callbacks import TensorBoard
import pickle
import numpy as np
import time
import os
#use this below code line only when you not have Nvidia Graphic Card and CUDA while training with GPU.
#os.environ["CUDA_VISIBLE_DEVICES"]="-1"    

NAME = "covid19_and_normal".format(int(time.time()))
PATH = os.path.join('logs', NAME)

gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction = 0.5)
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpu_options))
pickle_in_x = open("X.pickle","rb")
X = pickle.load(pickle_in_x)

pickle_in_y = open("Y.pickle","rb")
Y = pickle.load(pickle_in_y)

X=X/255.0           #normalising images pixel values

conv_layer = [3]
conv_size = [64]
dense_layer =[1]

NAME = '{}-conv_layer-{}-conv_size-{}-dense_layer'.format(conv_layer,conv_size,dense_layer, int(time.time()))
PATH = os.path.join('logs', NAME)
tensorboard = TensorBoard(log_dir=PATH, profile_batch = 0)

metrices =  [tf.keras.metrics.BinaryAccuracy(name='accuracy'),
			tf.keras.metrics.Precision(name='precision'),
			tf.keras.metrics.Recall(name='recall'),
			tf.keras.metrics.AUC(name='auc')]

model = Sequential()
model.add(Conv2D(64,(3,3),input_shape = X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.3)) 

model.add(Conv2D(64,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.3))   #giving and changing dropout is always useful as it helps to prevent overfitting

model.add(Conv2D(64,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.3))

model.add(Flatten())

model.add(Dense(64))
model.add(Activation("relu"))
model.add(Dropout(0.3))

model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = metrices)
model.fit(X,Y, batch_size = 8, epochs = 16, validation_split = 0.3, callbacks=[tensorboard])

model.save('covid19_pneumonia_detection_cnn.h5') #comment this line while using tensorboard for checking the performance of multiple model architectures by optimizing and changing values of parameters.