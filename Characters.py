import abc

# Super class for the player and character
class Character(abc.ABC):
    def __init__(self) -> None:
        self.hand = []
        self.value = 0

    def hit(self, deck):
        if len(deck.deck) < 1:
            print("Deck is empty.")
            return
        
        card = deck.deck.pop()
        self.hand.append(card)
        self.showHand()
    
    def showValue(self):
        return f"Total value - {self.value}"
    
    def getAceValue(self, currentValue, numAces):
        while currentValue > 21 and numAces > 0:
            currentValue -= 10
            numAces -= 1

        return currentValue
    
    @abc.abstractmethod
    def showHand(self):
        pass
    
    @abc.abstractmethod
    def handValue(self):
        pass



class Player(Character):
    def __init__(self, currency=150) -> None:
        super().__init__()
        self.currency = currency
    
    @property
    def currency(self) -> int:
        return self._currency
    
    @currency.setter
    def currency(self, value) -> int:
        if value > 0:
            self._currency = value


    def handValue(self) -> int:
        numAces = 0
        currentValue = 0

        for card in self.hand:
            currentValue += card[1]
            if "Ace" in card[0]:
                numAces += 1

        # If a player has an Ace and would bust
        # Ace value goes from 11 to 1
        currentValue = self.getAceValue(currentValue, numAces)
        
        self.value = currentValue

        return self.value

    def showHand(self) -> None:
        for card in self.hand:
            print(card[0])
        
        print(self.handValue())
        
        


class Dealer(Character):
    def __init__(self) -> None:
        super().__init__()
    
    def hit(self, deck, revealFull=False):
        if len(deck.deck) < 1:
            print("Deck is empty.")
            return
        
        card = deck.deck.pop()
        self.hand.append(card)
        self.showHand(revealFull)

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
        numAces = 0
        currentValue = 0

        # Only count the 2nd card's value until dealer reveals first card
        cardsToCount = self.hand if revealFull else self.hand[1:]
        
        for card in cardsToCount:
            currentValue += card[1]
            if "Ace" in card[0]:
                numAces += 1

        # When player has more than 1 Ace or would bust
        # Ace value goes from 11 to 1
        currentValue = self.getAceValue(currentValue, numAces)

        self.value = currentValue
        
        return self.value
    