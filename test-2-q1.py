#Problem 1:
#Create a program that includes the following:
#● A function that generates a list that represents all of the values in a
#standard deck of 52 cards (Links to an external site.)
#● A function that "shuffles the deck" (randomizes the items in your list)
#● A function that draws the first card from the deck (removes the card in the
#0th position)
#● Print out the cards left in the deck
#Sample output:
#My cards: 'Ace of Hearts', 'Ace of Diamonds', 'Ace of Spades', 'Ace of Clubs', '2 of
#Hearts', '2 of Diamonds',....
#My shuffled cards: '10 of Diamonds', '2 of Spades', '10 of Spades', '10 of Spades', '7 of
#Clubs', '3 of Spades', '5 of Diamonds', '9 of Hearts', '10 of Diamonds',....
#First card in the deck: 10 of Diamonds
#Cards left in the deck: '2 of Spades', '10 of Spades', '10 of Spades', '7 of Clubs', '3 of
#Spades', '5 of Diamonds', '9 of *Hearts', '10 of Diamonds',....\
import random
def generates():
    card1 = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    card2 = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck = []
    for i in card1:
        for j in card2:
            card = f"{j} of {i}"
            deck.append(card)    
    print("My cards:" , deck)
    random.shuffle(deck)
    print("My shuffled cards:" , deck)
    First_card = deck.pop(0)
    print("First card in the deck: " ,First_card)
    print("Cards left in the deck: " ,deck)
generates()  