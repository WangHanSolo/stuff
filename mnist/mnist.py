import utils
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
from matplotlib import pyplot as plt


images = utils.load_imgs()
labels = utils.load_labels()
size = len(images)

train_imgs = images[:int(size * 0.9)]
train_labels = labels[:int(size * 0.9)]
test_imgs = images[int(size * 0.9):]
test_labels = labels[int(size * 0.9):]


model = Sequential()
model.add(Conv2D(28, kernel_size=(3,3), input_shape = (28,28,1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(128, activation=tf.nn.relu))
model.add(Dropout(0.2))
model.add(Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x=train_imgs, y=train_labels, epochs=10)

model.evaluate(test_imgs, test_labels)