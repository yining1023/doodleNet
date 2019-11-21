# DoodleNet 

This is a series of experiments I did about Doodle Classifier(a Convolutional Neural Network) using tensorflow.js and tensorflow. The data I used is from [Quickdraw dataset](https://quickdraw.withgoogle.com/data).

Here are a list of the projects - 
1. Train a doodle classifier with [tf.js](https://www.tensorflow.org/js/)
2. Train a doodle classifier with 345 classes
3. KNN doodle classifier

## Credits: Big thanks to [@zaidalyafeai](https://github.com/zaidalyafeai)'s [sketcher](https://github.com/zaidalyafeai/zaidalyafeai.github.io/tree/master/sketcher) google colab for training.

## 1. Train a doodle classifier with tf.js
I trained a doodle classifier with 3 classes(bowtie, lollipop, rainbow) in the browser using tfjs' [layers API](https://github.com/tensorflow/tfjs-layers) and [tf.js-vis](https://github.com/tensorflow/tfjs-vis). The code is based on [tf.js Example - Training MNIST](https://github.com/tensorflow/tfjs-examples/tree/master/mnist).

<img src="https://raw.githubusercontent.com/yining1023/doodleNet/master/images/doodleNet_tfjs.gif">

Try a live demo [here](https://yining1023.github.io/doodleNet/demo/TrainDoodleClassifier).

Once you open the webpage, wait until the page load the data, train the model, evaluate the model. It will download two files: `myDoodleNet.json` and `myDoodleNet.weights.bin`. To test this model your self, you can load these two files back, and click on 'load model' button, then draw sth on the canvas, hit 'Guess' button to let model start guessing the drawing.

## 2. Train a doodle classifier with 345 classes
It's trained on all 345 categories from Quickdraw dataset, 50k images per class. It's trained with tensorflow, and ported to tf.js in the browser. Here is the training [notebook](https://github.com/yining1023/doodleNet/blob/master/doodleNet.ipynb).

***This notebook is heavily based on [@zaidalyafeai](https://github.com/zaidalyafeai)'s Sketcher [notebook](https://github.com/zaidalyafeai/Notebooks) on 100 classes.*** I expanded the data to 345 classes and added a few layers to improve the accurary on 345 classes.

I used [spell.run](https://spell.run/)'s remote GPU machine with big RAM to load all the data and train the model.

<img src="https://raw.githubusercontent.com/yining1023/doodleNet/master/images/doodleNet_345.gif">

Try a live demo [here](https://yining1023.github.io/doodleNet/demo/DoodleClassifier_345).

## 3. KNN doodle classifier: Customizable doodle classes
Based on the previous doodle classifier of 345 classes, I added KNN classifier to it, so people can customize their own doodle classes.

<img src="https://raw.githubusercontent.com/yining1023/doodleNet/master/images/doodleNet_knn.gif">

Try a live demo [here](https://yining1023.github.io/doodleNet/demo/DoodleClassifier_KNN).

You can draw 10+ circles and add them to class A, and draw 10+ lines and add them to class B, then let the model to guess your new drawing. You can define any other classes, it doesn't need to be circles or squares.

## Get started
To run each examples locally, open your terminal, type in the following commands:
```
$ git clone https://github.com/yining1023/doodleNet.git
$ cd doodleNet
$ python -m SimpleHTTPServer     # $ python3 -m http.server (if you are using python 3)
```
Go to `localhost:8000/demo` in your browser, you will see a directory list like this:
- DoodleClassifier_345/
- DoodleClassifier_KNN/
- TrainDoodleClassifier/

Click into each example to see the demo.
