import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM, TimeDistributed, Activation


def generate_text(model, length):
    ix = [np.random.randint(VOCAB_SIZE)]
    y_char = [ix_to_char[ix[-1]]]
    X = np.zeros((1, length, VOCAB_SIZE))
    for i in range(length):
        X[0, i, :][ix[-1]] = 1
        print(ix_to_char[ix[-1]], end="")
        ix = np.argmax(model.predict(X[:, :i + 1, :])[0], 1)
        y_char.append(ix_to_char[ix[-1]])
    return ('').join(y_char)


data = open('dataset_queen.txt', 'r').read()
# TODO: get a list of all unique characters
chars = 
# TODO: get the number of unique letters
VOCAB_SIZE = 

# TODO: create dictionaries that map index to letters and vice versa
ix_to_char = 
char_to_ix = 

# TODO: define the length of one sequence and calculate the number of sequences
SEQ_LENGTH = 
SEQ_NUMBER = 

# create vector representation of input and output
X = np.zeros((SEQ_NUMBER, SEQ_LENGTH, VOCAB_SIZE))
y = np.zeros((SEQ_NUMBER, SEQ_LENGTH, VOCAB_SIZE))
for i in range(0, SEQ_NUMBER):
    X_sequence = data[i * SEQ_LENGTH:(i + 1) * SEQ_LENGTH]
    X_sequence_ix = [char_to_ix[value] for value in X_sequence]
    input_sequence = np.zeros((SEQ_LENGTH, VOCAB_SIZE))
    for j in range(SEQ_LENGTH):
        input_sequence[j][X_sequence_ix[j]] = 1.
    X[i] = input_sequence

    # TODO: prepare output vectors
    

# define number of neurons in hidden layers
HIDDEN_DIM = 128

# define model
model = Sequential()
model.add(LSTM(HIDDEN_DIM, input_shape=(None, VOCAB_SIZE), return_sequences=True))
model.add(LSTM(HIDDEN_DIM, return_sequences=True))
model.add(LSTM(HIDDEN_DIM, return_sequences=True))
model.add(TimeDistributed(Dense(VOCAB_SIZE)))
model.add(Activation('softmax'))
model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

GENERATE_LENGTH = 100
# random generation
generate_text(model, GENERATE_LENGTH)

# train and test model
epoch_no = 0
while True:
    print('\n')
    model.fit(X, y, batch_size=48, verbose=2, epochs=1)
    epoch_no += 1
    generate_text(model, GENERATE_LENGTH)
