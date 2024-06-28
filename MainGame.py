from Characters import Player, Dealer
from Deck import Deck
from Constants import *
from time import sleep

# Gets a prompt and sanitizes input
# Handles exiting the game, running the giveMoney() function
def getInput(prompt, type=str):
    while True:
        userInput = input(prompt).strip().lower()
        command = checkCommand(userInput)

        if command == "exit":
            return command
        
        if command == "money":
            giveMoney()
            continue

        if type == int:
            try:
                return int(userInput)
            except ValueError:
                print("Value must be an integer.")
        else:
            return userInput

def checkCommand(answer) -> str:
    if answer in EXITCOMMANDS:
        return "exit"
    if answer == MONEYCOMMAND:
        return "money"
    if answer in PLAYERACTION:
        return answer

# Sets the initial game up
def intro():
    numDecks = getInput("How many decks would you like to be shuffled: ", int)
    if numDecks == "exit":
        return
    deck.lengthDeck = numDecks

    sleep(0.5)
    print("Shuffling Deck...")
    deck.generateDeck()
    sleep(1.5)
    print("Deck successfully shuffled!")

def giveMoney():
    amtMoney = getInput("\nHow much money would you like to be given: ", int)
    if amtMoney == "exit":
        return
    player.currency += int(amtMoney)

def getBet() -> int:
    while True:
        bet = getInput("\nHow much would you like to bet: ", int)
        if bet == "exit":
            return
        
        if bet > player.currency:
            print(f"You do not have ${bet}")

        elif bet < MINBET:
            print(f"Bet must higher than {MINBET}.")

        else:
            player.currency -= bet
            break
    
    return bet
    
def dealCards():
    for i in range(2):
        print("Dealer: ")
        dealer.hit(deck)
        print("\n")

        print("Player:")
        player.hit(deck)

        print("\n")
    
def getAction():
    while True:

        if player.value == 21:
            print("You got Blackjack!\n")
            return 
        
        elif player.value > 21:
            print("You busted\n")
            return
        
        action = getInput("What would you like to do: ")
        print("\n")
        if action == "exit":
            return
        
        if action == "hit":
            player.hit(deck)
        
        elif action == "stand":
            return
        
        else:
            player.hit(deck)
            return

def dealerDraw():
    # Dealer soft-stands at 17
    while dealer.handValue(True) < 17:
        if dealer.handValue(True) == 21:
            print("Dealer has Blackjack!\n")
            break
        elif dealer.handValue(True) > 21:
            print("Dealer has busted!\n")
            break
        print("Dealer Hits:")
        dealer.hit(deck, True)
    
    print("\n")

def revealCard():
    print(f"Dealer has {dealer.showHand(True)}")

def getWinner():
    dealerHand = dealer.handValue(True)
    playerHand = player.handValue()

    if playerHand == 21 and playerHand != dealerHand:
        return "Blackjack"

    elif playerHand > dealerHand:
        return "Won"
    
    elif dealerHand == playerHand:
        return "Tied"

    elif playerHand <= 21 and dealerHand > 21:
        return "Won"
    
    else:
        return "Loss"
    
# Pays the player based on if they won or not
def getPayout(winStatus, bet):
    if winStatus == "Won":
        bet *= 2
        player.currency += bet
        print(f"Congratulations, you won ${bet}")
        print(f"Your new balance is ${player.currency}")
        return
    
    # In blackjack, getting 21 has higher payout rate
    if winStatus == "BlackJack":
        bet = int(bet*2.5)
        player.currency += bet
        print(f"Congratulations, you won ${bet} by getting Blackjack!")
        print(f"Your new balance is ${player.currency}")
        return

    if winStatus == "Tied":
        player.currency += bet
        print(f"You tied with the dealer and got ${bet} back!")
        print(f"Your new balance is ${player.currency}")
        return
    
    if winStatus == "Loss":
        print(f"You lost ${bet} credits! ")
        print(f"Your new balance is ${player.currency}")
        return


def main():
    global player, dealer, deck 

    player = Player()
    dealer = Dealer()
    deck = Deck()

    running = True

    # Intro gets ran outside of loop so the deck isn't reshuffled after every game
    intro()

    # Main gameplay loop
    while running:
        bet = getBet()

        # Dealer deals the cards
        deal = dealCards()

        # Player decides whether to hit, stand, or double
        playerAction = getAction()

        # Dealer hits after player finalizes actions
        dealerHit = dealerDraw()

        # Determines winner
        winner = getWinner()

        # Decides the payout
        payout = getPayout(winner, bet)

        break

########################################## MAIN ##########################################
if __name__ == "__main__":
    main()
