import os
import time


class Card:
    """
    The object definition of Card happens here
    It sets suit, value and card value here
    """

    def __init__(self, suit, value, card_value):

        # Suit of the Card like Spades and Clubs
        self.suit = suit

        # Representing Value of the Card like A for Ace, K for King
        self.value = value

        # Score Value for the Card like 10 for King
        self.card_value = card_value


def deck():

    # The type of suit
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

    # The suit value
    suits_values = {
        "Spades": "\u2664",
        "Hearts": "\u2661",
        "Clubs": "\u2667",
        "Diamonds": "\u2662",
    }

    # The type of card
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # The card value
    cards_values = {
        "A": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
    }

    # The deck of cards
    deck = []

    # Loop for every type of suit
    for suit in suits:

        # Loop for every type of card in a suit
        for card in cards:

            # Adding card to the deck
            deck.append(Card(suits_values[suit], card, cards_values[card]))
    return deck


# to clear the terminal
def clear():
    os.system("clear")


# line for making UI clearer
def line():
    print(10 * "-")


def time_break():
    """
    As the compiler works really fast,
    it would get overwhelming for the player to read
    the data within fraction of seconds
    This timer gives the reader a breathing space
    to understand what's going on
    """
    counter = 3
    while counter > 0:
        print(f"{str(counter)} secs\n")
        time.sleep(1)
        counter -= 1


# Formatting purpose
def header_line(input_string):
    line()
    print(f" {input_string.upper()} ")
    line()


# utility function for split functionality
def check_duplicates(cards):
    card_values = []

    for card in cards:
        card_values.append(card.value)
    if len(card_values) != len(set(card_values)):
        print("Cards with same value found!")
        return 1
    else:
        return 0


# Test cases for all the user inputs
def input_validation(flag, player_cards=0):
    if flag == "bet":
        while 1:
            try:
                bet_val = input("\nPlease enter the bet amount. (max 100$):")
                bet_val = int(bet_val)
                if bet_val > 0 and bet_val <= 100:
                    break
                else:
                    print("Please enter a valid number!")
            except:
                print("Please enter a valid number!")
        return bet_val

    if flag == "split":
        while 1:
            try:
                split_flag = input("Would you like to split Y/N?: ")
                if split_flag.upper() == "Y":
                    print("press enter to continue")
                    break
                elif split_flag.upper() == "N":
                    print("Not splitting the cards")
                    break
                else:
                    print("Wrong choice! Try again")
            except:
                print("Wrong choice! Try again")
        return split_flag.upper()

    if flag == "players_no":
        while 1:
            try:
                players_no = int(input("Enter the number of players: "))
                if int(players_no) > 0 and int(players_no) < 7:
                    break
                else:
                    print("Please enter a valid number!")
                    print("Note that max of 6 players can play")
            except:
                print("Wrong choice! Try again")
        return players_no

    if flag == "rounds_no":
        while 1:
            try:
                round_no = int(input("Enter the number of rounds: "))
                if round_no > 0 and round_no < 7:
                    break
                else:
                    print("Please enter a valid number!")
            except:
                print("Wrong choice! Try again")
        return round_no


def print_cards(cards, hidden):
    """
    The fucntion that makes the "UI"
    """

    s = ""
    for card in cards:
        s = s + "\t ________________"
    if hidden:
        s += "\t ________________"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        if card.value == "10":
            s = s + "\t|  {}            |".format(card.value)
        else:
            s = s + "\t|  {}             |".format(card.value)
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|      * *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|    *     *     |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|       {}        |".format(card.suit)
    if hidden:
        s += "\t|          *     |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|         *      |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|        *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        if card.value == "10":
            s = s + "\t|            {}  |".format(card.value)
        else:
            s = s + "\t|            {}   |".format(card.value)
    if hidden:
        s += "\t|        *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|________________|"
    if hidden:
        s += "\t|________________|"
    print(s)

    print()
