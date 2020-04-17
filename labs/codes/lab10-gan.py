from __future__ import print_function, division

from keras.datasets import mnist
from keras.layers import Input, Dense, Reshape, Flatten
from keras.layers import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU
from keras.models import Sequential, Model
from tensorflow.keras.optimizers import Adam

import matplotlib.pyplot as plt

import numpy as np


class GAN():
    def __init__(self):
        # MNIST data are grayscale 28 x 28 images
        self.img_rows = 28
        self.img_cols = 28
        self.channels = 1
        self.img_shape = (self.img_rows, self.img_cols, self.channels)

        # size of the input noise
        self.latent_dim = 100

        optimizer = Adam(0.0002, 0.5)

        # build and compile the discriminator
        # it solves binary classification, so we use binary crossentropy
        self.discriminator = self.build_discriminator()
        self.discriminator.compile(
            loss='binary_crossentropy',
            optimizer=optimizer,
            metrics=['accuracy'])

        # build the generator
        self.generator = self.build_generator()

        # we add an input layer to the generator: random noise
        z = Input(shape=(self.latent_dim,))
        # we get the generator output image by using the noise as input
        img = self.generator(z)

        # in the combined network we do not adjust the discriminator's weights
        self.discriminator.trainable = False

        # the discriminator's output is a prediction on the generator's output
        validity = self.discriminator(img)

        # we create the combined model: set the input and output layers
        self.combined = Model(z, validity)
        self.combined.compile(loss='binary_crossentropy', optimizer=optimizer)

    def build_generator(self):
        model = Sequential()

        model.add(Dense(256, input_dim=self.latent_dim))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(512))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(1024))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(np.prod(self.img_shape), activation='tanh'))
        model.add(Reshape(self.img_shape))

        model.summary()

        noise = Input(shape=(self.latent_dim,))
        img = model(noise)

        return Model(noise, img)

    def build_discriminator(self):
        model = Sequential()

        model.add(Flatten(input_shape=self.img_shape))
        model.add(Dense(512))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(256))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(1, activation='sigmoid'))
        model.summary()

        img = Input(shape=self.img_shape)
        validity = model(img)

        return Model(img, validity)

    def train(self, epochs, batch_size=128, sample_interval=50):
        # we load the MNIST dataset, we only need the training input set
        (X_train, _), (_, _) = mnist.load_data()

        # we normalize the pixels to the scale from -1 to 1
        X_train = X_train / 127.5 - 1.
        X_train = np.expand_dims(X_train, axis=3)

        # expected outputs for the discriminator
        # batch_size number of ones for real images
        # batch_size number of zeroes for fake images
        valid = np.ones((batch_size, 1))
        fake = np.zeros((batch_size, 1))

        for epoch in range(epochs):

            #  we first train the discriminator

            # we select a random batch of images from the training set (real)
            idx = np.random.randint(0, X_train.shape[0], batch_size)
            imgs = X_train[idx]

            noise = np.random.normal(0, 1, (batch_size, self.latent_dim))

            # we generate a batch of new fake images
            gen_imgs = self.generator.predict(noise)

            # we train the discriminator and calculate the loss
            d_loss_real = self.discriminator.train_on_batch(imgs, valid)
            d_loss_fake = self.discriminator.train_on_batch(gen_imgs, fake)
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

            #  we then train the generator

            # we generate some random noise
            noise = np.random.normal(0, 1, (batch_size, self.latent_dim))

            # we traing the generator in the combined model
            # the discriminator's weights remain unchanged
            # we want the generator to generate images which
            # the discriminator will recognize as real
            g_loss = self.combined.train_on_batch(noise, valid)

            # we print some info about our progress
            print("{} [D loss: {}, acc.: {:.2f}%] [G loss: {}]".format(
                epoch, d_loss[0], 100 * d_loss[1], g_loss))

            # we save a sample of generated image after a few epochs
            if epoch % sample_interval == 0:
                self.sample_images(epoch)

    def sample_images(self, epoch):
        r, c = 5, 5
        noise = np.random.normal(0, 1, (r * c, self.latent_dim))
        gen_imgs = self.generator.predict(noise)

        # Rescale images 0 - 1
        gen_imgs = 0.5 * gen_imgs + 0.5

        fig, axs = plt.subplots(r, c)
        cnt = 0
        for i in range(r):
            for j in range(c):
                axs[i, j].imshow(gen_imgs[cnt, :, :, 0], cmap='gray')
                axs[i, j].axis('off')
                cnt += 1
        fig.savefig("images/{}.png".format(epoch))
        plt.close()


if __name__ == '__main__':
    training_epochs = 30000

    gan = GAN()
    gan.train(epochs=training_epochs, batch_size=32, sample_interval=200)
    gan.sample_images(training_epochs)
