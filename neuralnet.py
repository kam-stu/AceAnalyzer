# Class holds 2 neural networks - one being a custom neural net only utilizing numpy and pandas
# The reasoning for this is to gain knowledge on how a neural net works, then build a "traditional" neural net using
# Tensorflow
# The custom neural network will use 2 hidden layers with 16 and 8 nodes respectively
# The other neural networkw will use 3 hidden layers with 16, 8, and 8 nodes respectively
# I will prompt the user which neural network they would like to use and show the difference in confidence between the two


import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers, models

class NeuralNet:
    def __init__(self) -> None:
        self.data = pd.read_csv('blackjack_data.csv')
        self.data = np.array(self.data)

        # Gets the input type for inputs and outputs and maps it to x (input) and y (output)
        self.x = self.data[:, :3]
        self.y = self.data[:, 3:]


class Net(NeuralNet):
    def __init__(self) -> None:
        super().__init__()

        self.model = models.Sequential([
            layers.Dense(16, activation='relu', input_shape=(3,)),
            layers.Dense(8, activation='relu'),
            layers.Dense(8, activation='relu'),
            layers.Dense(3, activation='sigmoid')
        ])
    
        self.model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
    
    def train(self):
        self.model.fit(self.x, self.y, epochs=1000)
    
    def get_result(self, prediction):
        maxVal = 0.00
        maxIndex = 0
        for i in range(len(prediction)):
            print(f"testing i: {i}")
            for j in range(len(prediction[i])):
                print(f"testing j index: {j}")
                print(f"Testing j value: {prediction[0][j]}")
                print(f"="*50)
                if maxVal < prediction[0][j]:
                    maxVal = prediction[0][j]
                    maxIndex = j
                    print(f"MaxVal at end of loop {j} = {maxVal}")
                    print('='*50)
        
        print(f"MaxVal = {maxVal}")
        print(f"MaxIndex = {maxIndex}")
        print(f"="*50)

        if maxIndex == 0:
             print("Hit")
             return
        elif maxIndex == 1:
            print("Stand")
            return
        elif maxIndex == 2:
            print("Double")
            return
        else:
            print("Error")
            return

    
    def predict_manual(self, player_hand, dealer_hand, card_count):
        # Prepare the input data as a 2D array
        manual_input = np.array([[player_hand, dealer_hand, card_count]])
        
        # Predict the outcome (hit, stand, double)
        prediction = self.model.predict(manual_input)
        return prediction
class CustomNet(NeuralNet):
    def __init__(self) -> None:
        super().__init__()

        # Sets size for all the layers
        self.input_layer = self.x.shape[1]
        self.layer1_size = 16
        self.layer2_size = 8
        self.output_layer = self.y.shape[1]

        # Sets weights for all layers
        self.weights1 = np.random.rand(self.input_layer, self.layer1_size)
        self.weights2 = np.random.rand(self.layer1_size, self.layer2_size)
        self.weights3 = np.random.rand(self.layer2_size, self.output_layer)

        # Sets bias for all layers
        self.bias1 = np.random.rand(1, self.layer1_size)
        self.bias2 = np.random.rand(1, self.layer2_size)
        self.bias3 = np.random.rand(1, self.output_layer)


        self.learning_rate = 0.1
    
    def relu(self, z):
        return np.maximum(0, z)
    
    def relu_derivative(self, z):
        return z > 0
    
    def softmax(self, z):
        e_z = np.exp(z - np.max(z))  # Subtract the max for numerical stability
        return e_z / np.sum(e_z, axis=1, keepdims=True)

    def forward_prop(self):
        # Layer 1
        self.z1 = np.dot(self.x, self.weights1) + self.bias1
        self.a1 = self.relu(self.z1)

        # Layer 2
        self.z2 = np.dot(self.a1, self.weights2) + self.bias2
        self.a2 = self.relu(self.z2)

        # Layer 3
        self.z3 = np.dot(self.a2, self.weights3) + self.bias3
        self.a3 = self.softmax(self.z3)

    
    def back_prop(self):
        m = self.y.shape[0]
        loss = -np.sum(self.y * np.log(self.a3 + 1e-8)) / m

        # Output layer gradients
        dZ3 = self.a3 - self.y
        dW3 = 1 / m * dZ3.dot(self.a1.T)
        dB3 = 1 / m *np.sum(dZ3)
        
        #Hidden layer gradients
        dz2 = np.dot(dZ3, self.weights3.T) * (self.a2 > 0)  # ReLU derivative
        dw2 = np.dot(self.a1.T, dz2) / m  # Weight gradient for layer 2
        db2 = np.sum(dz2, axis=0, keepdims=True) / m  # Bias gradient for layer 2

            # Hidden layer 1 gradients
        dz1 = np.dot(dz2, self.weights2.T) * (self.a1 > 0)  # ReLU derivative
        dw1 = np.dot(self.x.T, dz1) / m  # Weight gradient for layer 1
        db1 = np.sum(dz1, axis=0, keepdims=True) / m  # Bias gradient for layer 1

            # Step 3: Update weights and biases
        self.weights1 -= self.learning_rate * dw1
        self.bias1 -= self.learning_rate * db1
        self.weights2 -= self.learning_rate * dw2
        self.bias2 -= self.learning_rate * db2
        self.weights3 -= self.learning_rate * dW3
        self.bias3 -= self.learning_rate * dB3

        return loss
    
    def train(self, epochs=1000):
        for epoch in range(epochs):
            self.forward_prop()

            loss = self.back_prop()

            if epoch % 100 == 0:
                print(f"Epoch: {epoch}, Loss: {loss:.4f}")

if __name__ == "__main__":
    custom_net = CustomNet()
    net = Net()
    prediction = net.predict_manual(0, 20, 0)
    net.get_result(prediction)


