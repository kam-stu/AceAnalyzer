from Characters import Player, Dealer
from NeuralNet import Net
from Deck import Deck
from Constants import *
from time import sleep

# Gets a prompt and sanitizes input
# Handles exiting the game, running the giveMoney() function
def getInput(prompt, type=str):
    global ai_toggle
    while True:
        userInput = input(prompt).strip().lower()
        command = checkCommand(userInput)

        sleep(0.5)

        if command == "exit":
            return command
        
        if command == "train":
            print("Training neuralNet!")
            sleep(0.75)
            neural_net.train()
            continue

        if command == "ai toggle":
            if ai_toggle:
                ai_toggle = False
                print(f"AI off")
            else:
                print(f"AI on")
                ai_toggle = True
            continue
        
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
    if answer == TRAINCOMMAND:
        return "train"
    if answer == AITOGGLECOMMAND:
        return "ai toggle"
    if answer in PLAYERACTION:
        return answer

# Sets the initial game up
def intro():
    print("Welcome to blackjack!!\n")
    sleep(1.5)
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

def getBet():
    global bet

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
        sleep(2)
        print("\n")

        print("Player:")
        player.hit(deck)
        sleep(2)

        print("\n")

def getAIAction():
    if ai_toggle:
        print(neural_net.predict(player.handValue(), dealer.handValue(), 0))
    
def getAction():
    global bet
    while True:

        if player.handValue() == 21:
            print("You got Blackjack!\n")
            return 
        
        elif player.handValue() > 21:
            print("You busted\n")
            return
        getAIAction()
        action = getInput("What would you like to do: ")
        print("\n")
        if action == "exit":
            return
        
        if action == "hit":
            print("Dealer:")
            dealer.showHand(False)
            print("")
            
            print("Player:")
            player.hit(deck)
        
        elif action == "stand":
            if dealer.handValue(True) >= 17:
                print("Dealer:\n")
                dealer.showHand(True)
            return
        
        elif action == "double":
            bet *= 2
            print("Player:")
            player.hit(deck)
            print("")
            print("Dealer:")
            dealer.showHand(True)
            return
            
        else:
            print("Not a known action.  Actions are: stand, hit, double")
        sleep(0.5)

def dealerDraw():
    # Dealer soft-stands at 17
    while dealer.handValue(True) < 17:
        print("Dealer Hits:")
        dealer.hit(deck, True)
        sleep(2)
    
    # Displays the result of the dealer busting
    # Or getting blackjack
    if dealer.handValue(True) == 21:
        print("Dealer has Blackjack!\n")
    elif dealer.handValue(True) > 21:
        print("Dealer busted!\n")

# Contains the logic for win conditions
def getWinner():
    dealerHand = dealer.handValue(True)
    playerHand = player.handValue()

    if playerHand == 21 and playerHand != dealerHand:
        return "Blackjack"

    elif playerHand <= 21 and playerHand > dealerHand:
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
    if winStatus == "Blackjack":
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

# Resets the hand so the player can play again
def reset_hands():
    player.hand = []
    dealer.hand = []

def main():
    global player, dealer, deck, neural_net, bet, ai_toggle

    player = Player()
    dealer = Dealer()
    deck = Deck()
    neural_net = Net()

    running = True
    ai_toggle = True

    # Intro gets ran outside of loop so the deck isn't reshuffled after every game
    intro()

    # If deck is empty, generates a new playing deck with a default length 
    # of 1 deck
    deck.checkDeck()

    # Main gameplay loop
    while running:
        bet = getBet()

        if bet == None:
            running = False
            return

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

        if player.currency == 0:
            print("Game over!  Better luck next time")
        
        reset_hands()

        deck.checkDeck()

########################################## MAIN ##########################################
if __name__ == "__main__":
    main()
