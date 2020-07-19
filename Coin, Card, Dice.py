#Intro: this code is designed to play hangman with the computer
##Date: 25/04/18
###Author: Manasi Mehta
import random
def Coin():
    coin = random.randrange(1,3)
    if coin == 1:
        coin = "tails"
    else:
        coin = "heads"
    print("The coin landed on " + coin)

def Dice():
    dice = random.randrange(1,7)
    print("The dice landed on " + str(dice))

def Card():
    suit = random.randrange(1,5)
    if suit == 1:
        suit = "Clubs"
    elif suit == 2:
        suit = "Hearts"
    elif suit == 3:
        suit = "Diamonds"
    else:
        suit = "Spades"
    number = random.randrange(1,14)
    if number == 1:
        number = "Ace"
    elif number == 11:
        number = "Jack"
    elif number == 12:
        number = "Queen"
    elif number == 13:
        number = "King"
    else:
        number = number
    print("The random card is " + str(number) + " of " + suit)
#####################################################
print("What is your name?")
username = input("?")
print ("Hi " + username + " welcome to the game coin, dice and card!")
canContinue = True
while (canContinue == True):
    print ("A: Coin")
    print ("B: Dice")
    print ("C: Card")
    print ("D: Quit ")
    print ("Choose: A,B,C,D")
    userOption = input ("?")
    if (userOption.upper() == "A"):
        Coin()
        
    elif (userOption.upper() == "B"):
        Dice()
        
    elif (userOption.upper() == "C"):
        Card()

    elif (userOption.upper() == "D"):
        print ("Ok! Goodbye!")
        canContinue = False
    else:
        print ("I do not understand " + userOption)
