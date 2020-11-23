from keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt


def plot_results(x_test, decoded_imgs, n=10):
    plt.figure(figsize=(40, 4))
    for i in range(n):
        # display original
        ax = plt.subplot(3, n, i + 1)
        plt.imshow(x_test[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # display reconstruction
        ax = plt.subplot(3, n, i + 1 + n * 2)
        plt.imshow(decoded_imgs[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()


(x_train, _), (x_test, _) = mnist.load_data()

x_train = # TODO: make type float32, normalize to interval 0 to 1
x_test = # TODO: make type float32, normalize to interval 0 to 1
x_train = # TODO: reshape
x_test = # TODO: reshape

input_img = # define input layer

encoded_1 = # define first convolution, activation relu, padding same
encoded_2 = # define max pooling layer, padding same
encoded_3 = # define second convolution, activation relu, padding same
encoded_4 = # define max pooling layer, padding same
encoded_5 = # define third convolution, activation relu, padding same
encoded = # define max pooling layer, padding same

decoded_1 = # define first decoding convolution, activation relu, padding same
decoded_2 = # define first upsampling layer
decoded_3 = # define second decoding convolution, activation relu, padding same
decoded_4 = # define second upsampling layer
decoded_5 = # define third decoding convolution, activation relu
decoded_6 = # define third upsampling layer
decoded = # define final decoding convolution, activation sigmoid, padding same

autoencoder = Model(input_img, decoded)

autoencoder.compile(# optimizer adadelta, loss function binary_crossentropy
    )

EPOCH_NO = 25
for x in range(EPOCH_NO):
    autoencoder.fit(# define parameters
        )

    decoded_imgs = autoencoder.predict(x_test)

    plot_results(x_test, decoded_imgs)
