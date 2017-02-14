import random


def gen_suit():
    suit = random.randint(1, 4)
    if suit == 1:
        return "Clubs"
    if suit == 2:
        return "Diamonds"
    if suit == 3:
        return "Hearts"
    if suit == 4:
        return "Spades"
    return "Whoops!"


def gen_rank():
    rank = random.randint(1, 13)
    if rank == 1:
        return "Ace"
    if rank == 11:
        return "Jack"
    if rank == 12:
        return "Queen"
    if rank == 13:
        return "King"
    return str(rank)


def draw_card():
    return gen_rank() + " of " + gen_suit()


def test():
    n = 0
    while n < 10:
        print(draw_card())
        n += 1


def value(card):
    position = card.find(" ")
    rank = card[0:position]
    # print( rank )
    if rank == "Ace":
        return 11
    if rank == "King" or rank == "Queen" or rank == "Jack":
        return 10
    return int(rank)


def hand():
    card1 = draw_card()
    card2 = draw_card()
    print(card1, ", ", card2, sep="")
    return value(card1), value(card2)


def hit_me():
    card = value(draw_card())
    print("The draw card is", card)
    return card


def the_game():
    card1, card2 = hand()
    print(card1, card2)
    total = card1 + card2
    if total <= 16:
        print("Hit me!")
        total += hit_me()
    elif 16 < total < 21:
        print("Don't hit me")
    elif total == 21:
        print("Blackjack!")

    print("The total is ", total)
    if total > 21:
        print("You've lost!")
    

the_game()
