# Class holds 2 neural networks - one being a custom neural net only utilizing numpy and pandas
# The reasoning for this is to gain knowledge on how a neural net works, then build a "traditional" neural net using
# Pre-exsting technology
# The custom neural network will use 2 hidden layers with 16 and 8 nodes respectively
# The other neural networkw will use 3 hidden layers with 16, 8, and 8 nodes respectively
# I will prompt the user which neural network they would like to use and show the difference in confidence between the two


import numpy as np
import pandas as pd

class NeuralNet:
    def __init__(self) -> None:
        self.data = pd.read_csv('blackjack_data.csv')
        self.data = np.array(self.data)

class CustomNet(NeuralNet):
    def __init__(self) -> None:
        super().__init__()

        # Gets the input type for inputs and outputs and maps it to x (input) and y (output)
        self.x = self.data[:, :3]
        self.y = self.data[:, 3:]

        # Sets size for all the layers
        self.input_layer = self.x.shape[1]
        self.layer1_size = 16
        self.layer2_size = 8
        self.output_layer = self.y.shape[1]

        # Sets weights for all layers
        self.weights1 = np.random.rand(self.input_layer, self.layer1_size)
        self.weights2 = np.random.rand(self.layer1_size, self.layer2_size)
        self.weights3 = np.random.rand(self.layer2_size, self.output_layer)

        self.learning_rate = 0.1
    
    def forward_prop(self):
        pass



custom_net = CustomNet()


