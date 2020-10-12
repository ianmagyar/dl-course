from keras.models import Sequential
from keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from keras.optimizers import Adam

from keras.datasets import mnist
from keras.utils import to_categorical

from sklearn.metrics import classification_report, confusion_matrix


# we load the dataset from keras
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# we set the image sizes for further use
img_height, img_width = 28, 28

# reshape the training and testing input sets - add a channel
# normalize input data to interval 0 - 1

# normalize (vectorize) output data

# define model, add layers based on the diagram
model = Sequential()

# check the model structure
model.summary()

# compile the model
model.compile()

# train the network
model.fit()

# evaluate the model
y_pred = model.predict(x_test)
matrix = confusion_matrix(y_test.argmax(axis=1), y_pred.argmax(axis=1))
print(matrix)
print(classification_report(y_test.argmax(axis=1), y_pred.argmax(axis=1)))
