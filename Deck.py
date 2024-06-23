import random

class Deck:
    def __init__(self) -> None:
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = {"Jack": 10, "Queen": 10, "King": 10, "9": 9, "8": 8, "7":7, "6":6, "5":5, "4": 4, "3": 3, "2": 2, "Ace": 11}

        # Sets the number of default decks that get shuffled into the played deck
        self.defaultLength = 1
        self.deck = []
    
    def generateDeck(self, numDecks) -> None:
        for i in range(numDecks):
            for suit in self.suits:
                for value, points in self.values.items():
                    cardName = f"{value} of {suit}"
                    self.deck.append((cardName, points))

        self.shuffleDeck() 
    
    def shuffleDeck(self) -> None:
        random.shuffle(self.deck)
    

    def checkDeck(self) -> None:
        if len(self.deck) < 1:
            print(f"Deck is empty. Generating a new deck with {self.defaultLength} number of decks")
            self.generateDeck(self.defaultLength)
            return
