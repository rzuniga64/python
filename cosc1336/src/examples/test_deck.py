import random

class deck:
    def __init__(self):
        self.__cards = [["2", "Spades"],["3", "Spades"],["4", "Spades"],["5", "Spades"],["6", "Spades"],
                        ["7", "Spades"],["8", "Spades"],["9", "Spades"],["10", "Spades"],["Jack", "Spades"],
                        ["Queen", "Spades"],["King", "Spades"],["Ace", "Spades"],["2", "Hearts"],["3", "Hearts"],
                        ["4", "Hearts"],["5", "Hearts"],["6", "Hearts"],["7", "Hearts"],["8", "Hearts"],
                        ["9", "Hearts"],["10", "Hearts"],["Jack", "Hearts"],["Queen", "Hearts"],["King", "Hearts"],
                        ["Ace", "Hearts"],["2", "Clubs"],["3", "Clubs"],["4", "Clubs"],["5", "Clubs"],
                        ["6", "Clubs"],["7", "Clubs"],["8", "Clubs"],["9", "Clubs"],["10", "Clubs"],
                        ["Jack", "Clubs"],["Queen", "Clubs"],["King", "Clubs"],["Ace", "Clubs"],
                        ["2", "Diamonds"],["3", "Diamonds"],["4", "Diamonds"],["5", "Diamonds"],["6", "Diamonds"],
                        ["7", "Diamonds"],["8", "Diamonds"],["9", "Diamonds"],["10", "Diamonds"],
                        ["Jack", "Diamonds"],["Queen", "Diamonds"],["King", "Diamonds"],["Ace", "Diamonds"]
                       ]

    def shuffle(self):
        random.shuffle(self.__cards)

    def draw_card(self, num):
        hand = []
        try:
            for i in range(num):
                hand.append(self.__cards.pop())
            return hand
        except:
            print("You have drawn too many cards please return the cards and shuffle again")

    def ret_card(self, cards):
        self.__cards += cards

    def display_deck(self):
        print(self.__cards)
        


if __name__ == "__main__":
    deck = deck()
    deck.display_deck()
    deck.shuffle()
    print("\n\n")
    hand = deck.draw_card(5)
    print(hand)
    print("\n\n")
    deck.display_deck()
    print("\n\n")
    deck.ret_card(hand)
    deck.display_deck()
    
