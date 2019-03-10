from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, AveragePooling2D
from keras.optimizers import Adam
from keras.losses import mean_squared_error

from keras.datasets import mnist
from keras.utils import to_categorical

from sklearn.metrics import confusion_matrix

(x_train, y_train), (x_test, y_test) = mnist.load_data()
img_height, img_width = 28, 28

x_train = x_train.reshape(# TODO)
x_test = x_test.reshape(# TODO)
input_shape = (# TODO)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model = Sequential()
# TODO add layers
model.summary()

model.compile(# TODO)

BATCH_SIZE = 128
EPOCHS = 1
model.fit(# TODO)

y_pred = model.predict(x_test)
matrix = confusion_matrix(y_test.argmax(axis=1), y_pred.argmax(axis=1))
print(matrix)
