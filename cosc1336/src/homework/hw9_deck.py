# Purpose: to create a deck of cards
# Input: A list of objects as a deck of cards
# Output: A hand dealt from the deck 

import hw9_card as Card
import random

numberInHand = 5

# Purpose: to create a deck of cards
# Output: the list of objects that is the deck
def createDeck(deck):
    # Create a dictionary with each card and its value 
    # stored as key-value pairs
    deck.append(Card.Card("2", "Spades"))
    deck.append(Card.Card("3", "Spades"))
    deck.append(Card.Card("4", "Spades"))
    deck.append(Card.Card("5", "Spades"))   
    deck.append(Card.Card("6", "Spades")) 
    deck.append(Card.Card("7", "Spades"))
    deck.append(Card.Card("8", "Spades"))
    deck.append(Card.Card("9", "Spades"))
    deck.append(Card.Card("10", "Spades"))    
    deck.append(Card.Card("Jack", "Spades"))         
    deck.append(Card.Card("Queen", "Spades"))
    deck.append(Card.Card("King", "Spades"))
    deck.append(Card.Card("Ace", "Spades"))
    deck.append(Card.Card("2", "Hearts"))
    deck.append(Card.Card("3", "Hearts"))   
    deck.append(Card.Card("4", "Hearts"))        
    deck.append(Card.Card("5", "Hearts"))
    deck.append(Card.Card("6", "Hearts"))
    deck.append(Card.Card("7", "Hearts"))
    deck.append(Card.Card("8", "Hearts"))    
    deck.append(Card.Card("9", "Hearts"))       
    deck.append(Card.Card("10", "Hearts"))
    deck.append(Card.Card("Jack", "Hearts"))
    deck.append(Card.Card("Queen", "Hearts"))
    deck.append(Card.Card("King", "Hearts"))   
    deck.append(Card.Card("Ace", "Hearts"))   
    deck.append(Card.Card("2", "Clubs"))
    deck.append(Card.Card("3", "Clubs"))
    deck.append(Card.Card("4", "Clubs"))
    deck.append(Card.Card("5", "Clubs"))   
    deck.append(Card.Card("6", "Clubs"))   
    deck.append(Card.Card("7", "Clubs"))
    deck.append(Card.Card("8", "Clubs"))
    deck.append(Card.Card("9", "Clubs"))
    deck.append(Card.Card("10", "Clubs"))    
    deck.append(Card.Card("Jack", "Clubs"))   
    deck.append(Card.Card("Queen", "Clubs"))
    deck.append(Card.Card("King", "Clubs"))
    deck.append(Card.Card("Ace", "Clubs"))
    deck.append(Card.Card("2", "Diamonds"))    
    deck.append(Card.Card("3", "Diamonds"))   
    deck.append(Card.Card("4", "Diamonds"))
    deck.append(Card.Card("5", "Diamonds"))
    deck.append(Card.Card("6", "Diamonds"))
    deck.append(Card.Card("7", "Diamonds"))    
    deck.append(Card.Card("8", "Diamonds"))   
    deck.append(Card.Card("9", "Diamonds"))
    deck.append(Card.Card("10", "Diamonds"))
    deck.append(Card.Card("Jack", "Diamonds"))
    deck.append(Card.Card("Queen", "Diamonds"))    
    deck.append(Card.Card("King", "Diamonds"))  
    deck.append(Card.Card("Ace", "Diamonds"))      

# Purpose: to create a hand dealt from the deck of cards
# Input: the list of ojbects that is the deck of cards,
#        the number of cards to be dealt
# Output: a number of cards called a hand
def dealCards(deck, number):
# Initialize an accumulator for the hand value.
    value = 0
    
    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck
    if number > len(deck):
        number = len(deck)
        
    # Deal the cards and accumulate their values
    # As the cards are dealt remove them from the deck
    hand = list()
    
    print("The hand that was dealt is:\n")
    for count in range(number):
        card = deck.pop()
        print(card)
        hand.append(card)
        value += card.getValue()
    print("\nThe value of the hand is: ", value)
        
    return hand
    
def main():
    # Create a deck of cards
    deck = list()
    createDeck(deck)
 
#   for card in deck:
#        print(card)
        
    random.shuffle(deck)
    
#    for card in deck:
#        print(card)

    #deal the cards
    hand = dealCards(deck, numberInHand)
    
main()