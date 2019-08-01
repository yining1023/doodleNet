from tensorflow import keras
import numpy as np
import cv2
import runway

# Read class names
with open("class_names.txt", "r") as ins:
  class_names = []
  for line in ins:
    class_names.append(line.rstrip('\n'))

# Load the model
model = keras.models.load_model('doodleNet-model.h5')
model.summary()

# open a local image
img = cv2.imread('umbrella.png')
img = cv2.resize(img, (28, 28))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = img.reshape((28, 28, 1))
img = (255 - img) / 255

# predict
pred = model.predict(np.expand_dims(img, axis=0))[0]
ind = (-pred).argsort()[:10]
latex = [class_names[x] for x in ind]
print(latex)
