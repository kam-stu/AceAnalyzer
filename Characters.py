class Player:
    def __init__(self) -> None:
        self.hand = []
        self.turn = 0
        self.currency = 0

    def hit(self, deck) -> None:
        if len(deck.deck) < 1:
            print("Deck is empty.")
            return
        
        card = deck.deck.pop()
        self.hand.append(card)
        self.showHand()

    def handValue(self) -> str:
        totalValue = 0
        numAces = 0

        for card in self.hand:
            totalValue += card[1]
            if "Ace" in card[0]:
                numAces += 1

        # If a player has an Ace and would bust
        # Ace value goes from 11 to 1
        while totalValue > 21 and numAces > 0:
            totalValue -= 10
            numAces -= 1

        return f"Total Value - {totalValue}\n"
    
    def showHand(self) -> None:
        for card in self.hand:
            print(card[0])
        
        print(self.handValue())
        
        


class Dealer(Player):
    def __init__(self) -> None:
        super().__init__()

    def showHand(self, revealFull=False) -> None:

        # Dealer doesn't reveal first card until after player stands
        if revealFull:
            for card in self.hand:
                print(card[0])
        else:
            print("Face-Down Card")
            for card in self.hand[1:]:
                print(card[0])
        
        print(self.handValue(revealFull))

    def handValue(self, revealFull=False) -> str:
        totalValue = 0
        numAces = 0

        # Only count the 2nd card's value until dealer reveals first card
        cardsToCount = self.hand if revealFull else self.hand[1:]
        
        for card in cardsToCount:
            totalValue += card[1]
            if "Ace" in card[0]:
                numAces += 1

        # When player has more than 1 Ace or would bust
        # Ace value goes from 11 to 1
        while totalValue > 21 and numAces > 1:
            totalValue -= 10
            numAces -= 1

        return f"Total Value - {totalValue}\n"