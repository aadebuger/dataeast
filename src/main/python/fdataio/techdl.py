'''
Created on 2018年3月19日

@author: aadebuger
'''


from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np


def testdata():
    
    data = np.random.random((1000, 5))
    labels = np.random.randint(2, size=(1000, 1))

def test1(data,labels):
    model = Sequential()
    model.add(Dense(32, activation='relu', input_dim=5))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='rmsprop',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    print(data)
    print(labels)
    model.fit(data, labels, epochs=10, batch_size=32)
    return model
def test2():
        model = Sequential()
        model.add(Dense(32, activation='relu', input_dim=100))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(optimizer='rmsprop',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
        data = np.random.random((1000, 100))
        labels = np.random.randint(2, size=(1000, 1))

# Train the model, iterating on the data in batches of 32 samples
model.fit(data, labels, epochs=10, batch_size=32)

# Train the model, iterating on the data in batches of 32 samples
model.fit(data, labels, epochs=10, batch_size=32)

model = Sequential([
Dense(32, units=784),
Activation('relu'),
Dense(10),
Activation('softmax'),
])


if __name__ == '__main__':
    pass