import random

Suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
Ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]


def create_deck():
    deck = []

    for suit in Suits:
        for rank in Ranks:
            card = str(rank) + " of " + suit
            deck.append(card)

    return deck


def shuffle(deck):
    for times in range(100):
        random_position = random.randint(1, 51)
        # Swap the value in element 0 with the random position.
        temp = deck[0]
        deck[0] = deck[random_position]
        deck[random_position] = temp


def deal(deck, n_cards):
    hand = []
    for n in range(n_cards):
        hand.append(deck[n])
    return hand


def give_rank(card):
    # Find first space in card names of the form: <rank> of <suit>
    space = card.find(" ")
    rank = card[0:space]
    return rank


def give_club_index(rank):
    if rank == "Ace":
        return 12
    if rank == "King":
        return 11
    if rank == "Queen":
        return 10
    if rank == "Jack":
        return 9
    return int(rank) - 2


def count_usage_in_hand(hand):
    rank_count = [0] * 13
    for card in hand:
        its_rank = give_rank(card)
        # Map names of ranks on each card (as strings) into integers 0..12.
        rank_index = give_club_index(its_rank)
        rank_count[rank_index] += 1
    return rank_count


def main():
    playing_cards = create_deck()
    shuffle(playing_cards)
    five_cards = deal(playing_cards, 5)
    print(five_cards)
    rank_counts = count_usage_in_hand(five_cards)
    print(rank_counts)

main()
