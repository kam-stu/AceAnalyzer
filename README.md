# AceAnalyzer
Game of Blackjack with an additional AI!

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [QoL Features](#qol-features)
- [Installation](#installation)
- [Usage](#usage)
- [Neural Network](#neural-network)
- [DataSet](#dataset)


## Introduction
This program is a fully functioning game of Blackjack.  You can choose the number of decks you'd like to have shuffled, bet a certain amount, and can play back-to-back with different bets.  
The reason behind making this program was adding a neural network that can help the player play Blackjack by giving them the ideal move at any given situation.  At the moment, the Neural Network can only make decisions based off of basic info (player hand and dealer hand), but over time and gathering more data, I'd like to be able to modify the neural network to take the card count (method of determining what cards are more likely to appear to "beat the odds") into account so the user is given a much more detailed action that may not align to "normal" Blackjack plays.

## Features
- Currency system for betting
- Play against a dealer repeatedly
- In-game Commands
- Stand, hit, double actions

## QoL Features
- !train - Trains AI model
- !giveMoney() - User can give themself more money
- !ai - Toggles the AI that tells you the best move

## Installation

1. Clone the repository:
```bash
git clone https://https://github.com/kam-stu/AceAnalyzer
```

2. Navigate to the project directory:
```bash
cd AceAnalyzer
```

3. Install dependenies:
```bash
pip install -r requirements.txt
```

4. Train AI (Recommended Method):
```bash
python NeuralNet.py
```

5. Run the game:
```bash
python MainGame.py
```

```
Alternatively you can run MainGame.py/NeuralNet.py in an IDE
```

6. Train AI (Alternate Method):
```
use !train command before game fully starts
```


## Usage

1. Start the game
```bash
python MainGame.py
```

```
Alternatively you can run MainGame.py in an IDE
```

2. You'll be asked how many decks to shuffle.  Enter the number and follow prompts.
```
How many decks would you like to be shuffled: 2
```

3. Place your bet (10 bet minimum):
```
How much would you like to bet: 50
```

4. Perform actions like hitting, standing, or doubling.  Alternatively "Exit" or any of the QoL commands
```
What would you like to do: hit
```

5. After the dealer completes their turn, the game will display the result of the game and update your balance acoordingly

## Neural Network
AceAnalyzer contains a Neural Network.  The outline and way it works will be discussed in this section.  Simply skip this section if you do not care about the Nueral Network in detail.

This neural network is built using Tensorflow and Tensorflow Keras.  I would like to implement a custom neural network using purely the math that goes along with a neural network only using the NumPy library.  However, due to current circumastances with school work, I am unable to put in the time and effort into learning and implementing custom neural networks.

The input layer for the network contains 3 nodes:
- player hand value
- dealer hand value
- card count (going to be used for future purposes when card counting gets implemented)

The network has 3 hidden layers with
- 16 Nodes
- 8 Nodes
- 8 Nodes

Finally, the output layer contains 3 nodes
- Value (0 -> 1) for Hitting
- Value (0 -> 1) for Standing
- Value (0 -> 1) for Doubling

The network contains 3 major methods:
- train()
- predict()
- get_result()

Predict() function makes a prediction given 3 values:
- player hand value
- dealer hand value
- current count (always set to 0 for now until implementation)
then returns a list of the values of the output layer

Get_result() function takes a prediction and finds the index value of the highest number (desired output) and returns it.  This is done by getting a minimum value and matching it with its index.

## Dataset
This section is going to talk more about the dataset and how it was made.  Skip this section if you aren't interested.  

The datset is a custom set that I made myself based off of normal Blackjack strategies.  Due to how small the dataset is, the neural network is unable to become very accurate (98% accuracy+).  This is not the networks fault.  The dataset in use is relatively small compared to the size of a desired dataset; however, the set has every strategy within it and repeated 3 times extra as that's all that I am currently able to do without implementing card counting, which would make things awkward as I do not card count nor know the strategies for card counting myself.

If you would like to help improve the datast by optimizing it, making it bigger, or adding card counting strategies, feel free to email me at my [email](kstuckey817@gmail.com) or any of the other means of communication that exist on my [website](https://kamstu.com)