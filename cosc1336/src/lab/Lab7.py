import random

Suits = [ "Clubs", "Diamonds", "Hearts", "Spades" ]
Ranks = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace" ]

def createDeck():
    deck = []

    for suit in Suits:
        for rank in Ranks:
            card = str( rank ) + " of " + suit
            deck.append( card )

    return deck

def shuffle( deck ):
    for times in range( 100 ):
        randomPosition = random.randint( 1, 51 )
        # Swap the value in element 0 with the random position.
        temp = deck[0]
        deck[0] = deck[randomPosition]
        deck[randomPosition] = temp

def deal( deck, nCards ):
    hand = []
    for n in range( nCards ):
        hand.append( deck[n] )
    return hand

def giveRank( card ):
    # Find first space in card names of the form: <rank> of <suit>
    space = card.find( " " )
    rank = card[0:space]
    return rank

def giveClubIndex( rank ):
    if rank == "Ace":
        return 12
    if rank == "King":
        return 11
    if rank == "Queen":
        return 10
    if rank == "Jack":
        return 9
    return int( rank ) - 2

def countUsageInHand( hand ):
    rankCount = [ 0 ] * 13
    for card in hand:
        itsRank = giveRank( card )
        # Map names of ranks on each card (as strings) into integers 0..12.
        rankIndex = giveClubIndex( itsRank )
        rankCount[rankIndex] += 1
    return rankCount

def main():
    playingCards = createDeck()
    shuffle( playingCards )
    fiveCards = deal( playingCards, 5 )
    print( fiveCards )
    rankCounts = countUsageInHand( fiveCards )
    print( rankCounts )

main()
