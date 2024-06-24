from Characters import Player, Dealer
from Deck import Deck
from Constants import *
from time import sleep

# Gets a prompt and sanitizes input
# Handles exiting the game, running the giveMoney() function, and playerAction (hit, stand, double)
def getInput(prompt, type=str, allowActions=False):
    while True:
        userInput = input(prompt).strip().lower()
        command = checkCommand(userInput)

        if command == "exit":
            return command
        
        if command == "money":
            giveMoney()
            continue

        elif command in PLAYERACTION and allowActions:
            if command == "hit":
                player.hit()
                return

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

# Pays the player based on if they won or not
def payout(winStatus, bet):
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
        print(f"You tied with the dealer and got ${bet} back!")
        print(f"Your new balance is ${player.currency}")
        return
    
    if winStatus == "Loss":
        print(f"You lost ${bet} credits! ")
        print(f"Your new balance is ${player.currency}")
        return
    

########################################## MAIN ##########################################

player = Player()
dealer = Dealer()
deck = Deck()

running = True

# Intro gets ran outside of loop so the deck isn't reshuffled after every game
intro()

# Main gameplay loop
while running:
    playerBet = getBet()
    break