from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import SimpleRNN, Dense
import numpy as np
import os

class NumberPredictor:
    def __init__(self, num_epochs=200, model_path='model.h5'):
        self.num_epochs = num_epochs
        self.model_path = model_path
        if os.path.exists(self.model_path):
            self.model = load_model(self.model_path)
        else:
            self.model = Sequential([
                SimpleRNN(50, activation='tanh', return_sequences=True, input_shape=(10, 1)),
                SimpleRNN(50, activation='tanh', return_sequences=True),
                SimpleRNN(50, activation='tanh'),
                Dense(50, activation='relu'),
                Dense(1)
            ])
            self.model.compile(optimizer='adam', loss='mean_squared_error')

    def train(self):
        if not os.path.exists(self.model_path):
            # Create sequences of 11 consecutive numbers from 1 to 1,000,000
            sequences = np.array([range(i, i+11) for i in range(1, 1000001)])

            # Split each sequence into input (first 10 numbers) and output (last number)
            X = sequences[:, :-1]
            y = sequences[:, -1]

            X = X.reshape((X.shape[0], X.shape[1], 1))
            self.model.fit(X, y, epochs=self.num_epochs, batch_size=1024)
            self.model.save(self.model_path)

    def predict_next_10(self, n):
        input = np.array([i for i in range(n, n+10)]).reshape((1, 10, 1))
        predictions = []
        for _ in range(10):
            prediction = self.model.predict(input)
            predictions.append(prediction[0][0])
            input = np.roll(input, -1)
            input[0, -1, 0] = prediction
        return predictions