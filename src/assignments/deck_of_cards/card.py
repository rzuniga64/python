# Purpose: To create a card of a certain rank and suit
#          that has a certain value
# Input: the suit and rank
# Output: card with a suit, rank and value

class Card:
    
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit
        if self.__rank == "2":
            self.__value = 0
        elif self.__rank == "3":
            self.__value = 1        
        elif self.__rank == "4":
            self.__value = 2
        elif self.__rank == "5":
            self.__value = 3
        elif self.__rank == "6":
            self.__value = 4
        elif self.__rank == "7":
            self.__value = 5
        elif self.__rank == "8":
            self.__value = 6
        elif self.__rank == "9":
            self.__value = 7
        elif self.__rank == "10":
            self.__value = 8
        elif self.__rank == "Jack":
            self.__value = 9
        elif self.__rank == "Queen":
            self.__value = 10
        elif self.__rank == "King":
            self.__value = 11
        elif self.__rank == "Ace":
            self.__value = 12
        
    def display(self):
        print(self.__rank, self.__suit)
        
    def __str__(self):
        return self.__rank + " of " + self.__suit + " equals " + str(self.__value)
    
    def getRank(self):
        return self.__rank
    
    def getSuit(self):
        return self.__suit
    
    def getValue(self):
        return self.__value
    
    def setRank(self, rank):
        self.__rank = rank
        
    def setSuit(self, suit):
        self.__suit = suit
        
        
        
        
    