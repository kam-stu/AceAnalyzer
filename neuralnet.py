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
from sklearn.model_selection import train_test_split

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
            layers.Dense(3, activation='softmax')
        ])
    
        self.model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
    
    def train(self):
        #Splits the data 80/20 to training and testing sets
        x_train, x_test, y_train, y_test = train_test_split(self.x, self.y, test_size=0.2, random_state=42, shuffle=True)
        
        # Trains the model
        self.model.fit(x_train, y_train, epochs=1500, verbose=1)

        # Evaluate the model on the test set
        test_loss, test_accuracy = self.model.evaluate(x_test, y_test, verbose=1)
        print(f'Test Loss: {test_loss}, Test Accuracy: {test_accuracy}')
    
    # Takes the prediction and rturns the desired output based on the index
    # with the highest value (indicating desired output)
    def get_result(self, prediction):
        maxVal = 0.00
        maxIndex = 0

        for i in range(len(prediction)):
            for j in range(len(prediction[i])):
                if maxVal < prediction[0][j]:
                    maxVal = prediction[0][j]
                    maxIndex = j

        if maxIndex == 0:
            return "Stand"
        elif maxIndex == 1:
            return "Hit"
        elif maxIndex == 2:
            print("Double")
            return

    
    def predict(self, player_hand, dealer_hand, card_count):
        # Prepare the input data as a 2D array
        input = np.array([[player_hand, dealer_hand, card_count]])
        
        # Predict the outcome (hit, stand, double)
        prediction = self.model.predict(input)

        result = self.get_result(prediction)

        return result
    
if __name__ == "__main__":
    net = Net()
    net.train()


