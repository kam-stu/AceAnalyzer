from Characters import Player, Dealer
from Deck import Deck

if __name__ == "__main__":
    testDeck = Deck()
    testPlayer = Player()
    testDealer = Dealer()

    testDeck.generateDeck(testDeck.defaultLength)

    testPlayer.hit(testDeck)
    testDealer.hit(testDeck)
    testDealer.hit(testDeck)

    testDealer.showHand(True)
