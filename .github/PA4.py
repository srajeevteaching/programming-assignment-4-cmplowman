#Chris Plowman
#Programming assignment 4
#11/10/21
#CS -151

import random

def generate_shuffled_deck():
    deck = []

    suits = "cdhs"
    for s in suits:
        for i in range (1,14):
            deck.append(str(i)+s)
    random.shuffle(deck)
    return deck

def card_as_string(card):
    s = " "
    value = card[0:-1]
    if value == "1":
        s += "Ace"
    elif value == "11":
        s += "Jack"
    elif value == "12":
        s += "King"
    else:
        s += value
    s += " of "

    suit = card[-1]
    if suit == "c":
        s += "clubs"
    elif suit == "d":
        s += "diamonds"
    elif suit == "h":
        s += "hearts"
    else:
        s += "spades"

    return s

def print_hand(hand):
    for card in hand:
        print(card_as_string(card))

def hand_value(hand):
    value = 0
    for card in hand:
        points = int(card[0:-1])
        if points in range(11,14):
            value += 10
        elif points == 1:
            value += 11
        else:
            value += points
    return value

def print_hands_with_totals(player_hand, dealer_hand):
    print("Player")
    print_hand(player_hand)
    print("total: " + str(hand_value(player_hand)))
    print("Dealer")
    print_hand(dealer_hand)
    print("total: " + str(hand_value(dealer_hand)))

def main():

    deck = generate_shuffled_deck()

    dealer_hand = []
    player_hand = []

    player_hand.append(deck.pop())
    player_hand.append(deck.pop())
    print_hand(player_hand)

    game_over = False
    while not game_over:
        choice = input("press [h] to hit, press [s] to stop playing: ")
        if choice not in ["h","s"]:
            continue
        if choice == "s":
            break
        player_hand.append(deck.pop())
        print_hand(player_hand)
        value = hand_value(player_hand)
        if value == 21:
            print("Blackjack!")
        elif value > 21:
            print("Bust!")
            game_over = True
    if not game_over:
        dealer_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

        while hand_value(dealer_hand) <= 17:
            dealer_hand.append(deck.pop())
            print_hands_with_totals(player_hand, dealer_hand)
        if hand_value(dealer_hand) > 21:
            print("Dealer Bust!")
        elif hand_value(player_hand) > hand_value(dealer_hand):
            print("Player Wins!")
        else:
            print("Dealer Wins!")
main()