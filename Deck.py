import random

class Deck:
    def __init__(self) -> None:
        self.suites = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = {"Jack": 10, "Queen": 10, "King": 10, "9": 9, "8": 8, "7":7, "6":6, "5":5, "4": 4, "3": 3, "2": 2, "Ace": 11}
        self.deck = []


        for suit in self.suites:
            for value, points in self.values.items():
                card_name = f"{value} of {suit}"
                self.deck.append((card_name, points))

        self.shuffleDeck()
    
    def shuffleDeck(self) -> None:
        self.tempDeck = []

        for i in range(len(self.deck)):
            card = random.choice(self.deck)
            self.tempDeck.append(card)
            self.deck.remove(card)
        
        self.deck = self.tempDeck
    
    # Test the deck
    def checkDeck(self) -> None:
        for card in self.deck:
            print(card)

class Player:
    def __init__(self) -> None:
        self.hand = []
        self.turn = 0
        self.currency = 0

    def hit(self, deck) -> None:
        card = deck.deck.pop()
        self.hand.append(card)

    def handValue(self) -> int:
        totalValue = 0
        numAces = 0

        for card in self.hand:
            totalValue += card[1]
            if "Ace" in card[0]:
                numAces += 1

        # When player has more than 1 Ace or would bust
        # Ace value goes from 11 to 1
        while totalValue > 21 and numAces > 1:
            totalValue -= 10
            numAces -= 1

        return totalValue
    
    def checkHand(self) -> None:
        for card in self.hand:
            print(card)

    def checkValue(self) -> None:
        print(self.handValue())

if __name__ == "__main__":
    testDeck = Deck()
    testPlayer = Player()

    testPlayer.hit(testDeck)

    testPlayer.checkValue()

    testPlayer.hit(testDeck)

    testPlayer.checkValue()

    testPlayer.hit(testDeck)
    testPlayer.checkValue()



