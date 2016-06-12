import test_deck


def display_hand(hand):
    for card in hand:
        print(card[0], card[1])


def assign_values(hand):
    card_num = 0
    for card in hand:
        if card[0] == "2":
            value = 0
        elif card[0] == "3":
            value = 1        
        elif card[0] == "4":
            value = 2
        elif card[0] == "5":
            value = 3
        elif card[0] == "6":
            value = 4
        elif card[0] == "7":
            value = 5
        elif card[0] == "8":
            value = 6
        elif card[0] == "9":
            value = 7
        elif card[0] == "10":
            value = 8
        elif card[0] == "Jack":
            value = 9
        elif card[0] == "Queen":
            value = 10
        elif card[0] == "King":
            value = 11
        elif card[0] == "Ace":
            value = 12

        hand[card_num].append(value)
        card_num += 1


def main():
    while True:
        choice = input("""
                           (N)ew game
                           (D)isplay hand
                           (H)it
                           (S)tay
                           (Q)uit_____
                                      :""").upper()
        if choice == "N":
            deck = test_deck.deck()
            deck.shuffle()
            hand = deck.draw_card(2)
            
        elif choice == "D":
            display_hand(hand)
        
        elif choice == "H":
            hand = deck.draw_card(1)
            
        elif choice == "S":
            pass

        elif choice == "Q":
            break
        
        else:
            print("Incorrect menu option please try again...")
               
    deck.display_deck()
    deck.shuffle()
    hand = deck.draw_card(5)
    display_hand(hand)
    assign_values(hand)
    print(hand)
    val_sum = 0
    for card in hand:
        val_sum += card[2]

    print("\n", val_sum)

if __name__ == "__main__":
    main()
