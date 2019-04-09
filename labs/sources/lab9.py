from keras.layers import Input, Dense
from keras.models import Model
from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np


def plot_results(x_test, encoded_imgs, decoded_imgs, n=10):
    plt.figure(figsize=(40, 4))
    for i in range(n):
        # display original
        ax = plt.subplot(3, n, i + 1)
        plt.imshow(x_test[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # display encoded
        ax = plt.subplot(3, n, i + 1 + n)
        plt.imshow(encoded_imgs[i].reshape(8, 4))
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


(mnist_train, _), (mnist_test, _) = mnist.load_data()

x_train = # TODO: normalize to range 0 to 1
x_test = # TODO: normalize to range 0 to 1
x_train = # TODO: reshape to a list of one-dimensional vectors
x_test = # TODO: reshape to a list of one-dimensional vectors

# simple autoencoder
input_img = # TODO: define input layer
encoded = # TODO: define hidden layer; activation relu
decoded = # TODO: define output layer; activation sigmoid

autoencoder = # TODO: define autoencoder
encoder = # TODO: define encoder

encoded_input = # TODO: define input to decoder
decoder_layer = # TODO: define further layer of decoder
decoder = # TODO: define decoder

autoencoder.compile(# TODO: insert parameters: optimizer, loss
    )
autoencoder.fit(# TODO: insert parameters: input, output, epochs, batch_size, shuffle
    )

encoded_imgs = encoder.predict(x_test)
decoded_imgs = autoencoder.predict(x_test)

plot_results(x_test, encoded_imgs, decoded_imgs)

# deep autoencoder
input_img = # TODO: define input layer
encoded_1 = # TODO: define next layer; activation relu
encoded_2 = # TODO: define next layer; activation relu
encoded_3 = # TODO: define next layer; activation relu

decoded_1 = # TODO: define next layer; activation relu
decoded_2 = # TODO: define next layer; activation relu
decoded_3 = # TODO: define next layer; activation sigmoid

autoencoder = # TODO: define autoencoder

encoder = # TODO: define encoder

encoded_input = # TODO: define input to decoder
decoder_layer = # TODO: define next layer of the decoder
decoder_layer = # TODO: define next layer of the decoder
decoder_layer = # TODO: define next layer of the decoder
decoder = # TODO: define decoder

autoencoder.compile(# TODO: insert parameters: optimizer, loss
    )
autoencoder.fit(# TODO: insert parameters: input, output, epochs, batch_size, shuffle
    )

encoded_imgs = encoder.predict(x_test)
decoded_imgs = decoder.predict(encoded_imgs)

plot_results(x_test, encoded_imgs, decoded_imgs)
