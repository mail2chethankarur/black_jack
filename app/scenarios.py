import random
import time
from utils import *


def split(player_cards, player_score):
    """
    To take user decsion on splitting.
    If chosen yes, this function splits the player's card and returns
    """

    set1, set2 = [], []
    set1.append(player_cards[0])
    set2.append(player_cards[1])
    player_cards1 = set1
    player_cards2 = set2
    return (player_cards1, player_cards2)


def pl_round(deck, player_score, player_cards, player_no):
    """
    This function is to define each player's round
    It also takes inputs for Hit/Stand
    """
    print("PLAYER CARDS: ")
    print_cards(player_cards, False)
    print(f"PLAYER {player_no} SCORE = ", player_score)

    # Managing the player moves
    while player_score < 21:
        choice = input("Enter H to Hit or S to Stand : ")

        # Sanity checks for player's choice
        if len(choice) != 1 or (choice.upper() != "H" and choice.upper() != "S"):
            print("Wrong choice!! Try Again")

        # If player decides to HIT
        if choice.upper() == "H":
            # Dealing a new card
            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)

            # Updating player score
            player_score += player_card.card_value

            # Updating player score in case player's card have ace in them
            c = 0
            while player_score > 21 and c < len(player_cards):
                if player_cards[c].card_value == 11:
                    player_cards[c].card_value = 1
                    player_score -= 10
                    c += 1
                else:
                    c += 1

            print("PLAYER CARDS: ")
            print_cards(player_cards, False)
            print("PLAYER SCORE = ", player_score)

        # If player decides to Stand
        if choice.upper() == "S":
            break
    if player_score > 21:
        print(f"PLAYER {player_no} BUSTED!")
    elif player_score == 21:
        print(f"PLAYER {player_no} has 21. \nLet's see if Bank gets 21!")

    return (deck, player_score)


def player(deck, player_no, bank_cards=0, bank_score=0):
    """
    Function for each player
    Arguments:-
    deck: the deck passed from the main function
    the same deck gets returned in the end so that the
    next player can continue with same deck

    player_no: Player's identity number

    bank_cards: default value is zero for first player
    as the bank open it's cards only after player 1 starts playing

    bank_score: current score that the bank has
    """
    time_break()
    clear()
    # Cards for both bank and player
    player_cards = []
    splt_decision = 0

    if bank_cards == 0:
        bank_cards = []
        bank_score = 0
        bank_flag = 0
    else:
        bank_flag = 1

    # Scores for both bank and player
    player_score = 0

    # Initial dealing for player and bank
    while len(player_cards) < 2:

        if len(player_cards) == 1:
            bet_val = input_validation("bet")

        # Randomly dealing a card
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)

        # Updating the player score
        player_score += player_card.card_value

        # In case both the cards are Ace, make the first ace value as 1
        if len(player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10

        # Print player cards and score
        print(f"PLAYER {player_no} CARDS: ")
        print_cards(player_cards, False)
        print(f"PLAYER {player_no} SCORE = ", player_score)

        input()

        if bank_flag == 0:
            # Randomly dealing a card
            bank_card = random.choice(deck)
            bank_cards.append(bank_card)
            deck.remove(bank_card)

            # Updating the bank score
            bank_score += bank_card.card_value

        # Print bank cards and score, keeping in mind to hide the second card and score
        print("BANK CARDS: ")
        if len(bank_cards) == 1:
            print_cards(bank_cards, False)
            print("BANK SCORE = ", bank_score)
        else:
            print_cards(bank_cards[:-1], True)
            print("BANK SCORE = ", bank_score - bank_cards[-1].card_value)

        # In case both the cards are Ace, make the second ace value as 1
        if len(bank_cards) == 2:
            if bank_cards[0].card_value == 11 and bank_cards[1].card_value == 11:
                bank_cards[1].card_value = 1
                bank_score -= 10

        if len(player_cards) == 2:
            # FOR TEST PURPOSE
            # player_cards[0].value='K'
            # player_cards[1].value='K'

            # Checking for split option
            dup_flag = check_duplicates(player_cards)
            if dup_flag:
                split_flag = input_validation("split")

                if split_flag == "Y":
                    split1, split2 = split(player_cards, player_score)
                    splt_decision = 1

    # Player gets a blackjack
    if player_score == 21:
        return (deck, bank_cards, bank_score, bet_val, player_score)

    if dup_flag and splt_decision == 1:
        print(f"Player {player_no} round 1 split 1: ")
        deck, score1 = pl_round(deck, int(player_score / 2), split1, player_no)
        line()
        print(f"Player {player_no} round 1 split 2: ")
        deck, score2 = pl_round(deck, int(player_score / 2), split2, player_no)
        line()
        return (deck, bank_cards, bank_score, bet_val, score1, score2)
    else:
        deck, player_score = pl_round(deck, player_score, player_cards, player_no)
        return (deck, bank_cards, bank_score, bet_val, player_score, 0)


def reveal_bank_cards(deck, player_no, bank_cards, bank_score):
    """
    This function is to reveal bank cards
    revealing happens only after all the players finish their turn
    and if all players are busted, this function is skipped
    """
    print()
    print("BANK IS REVEALING THE CARDS....")

    print("BANK CARDS: ")
    print_cards(bank_cards, False)
    print("BANK SCORE = ", bank_score)

    # Managing the bank moves
    while bank_score < 17:

        print("BANK DECIDES TO HIT.....")
        time.sleep(3)

        # Dealing card for bank
        bank_card = random.choice(deck)
        bank_cards.append(bank_card)
        deck.remove(bank_card)

        # Updating the bank's score
        bank_score += bank_card.card_value

        # Updating player score in case player's card have ace in them
        c = 0
        while bank_score > 21 and c < len(bank_cards):
            if bank_cards[c].card_value == 11:
                bank_cards[c].card_value = 1
                bank_score -= 10
                c += 1
            else:
                c += 1

        print("BANK CARDS: ")
        print_cards(bank_cards, False)
        print("BANK SCORE = ", bank_score)

    return bank_score


def get_game_stats(player_profile, bank_score):
    """
    To print the summary of the gane towards the end
    """
    line()
    print("game results:".upper())
    line()

    if bank_score > 21:
        print("Bank Busted!!! All Players Win!!!")
    elif bank_score == 21:
        print("BANK HAS A BLACKJACK!!! All Players Lose")
    else:
        for i in player_profile.keys():
            player_bet = player_profile[i][0]
            player_score = player_profile[i][1]
            player_status = player_profile[i][2]
            if player_status == "PLAYING":
                if player_score > bank_score:
                    print(f"PLAYER {str(i)} Won. Banks pays: {player_bet}")
                else:
                    print(f"PLAYER {str(i)} Lost. Player loses: {player_bet}")


def evaluate_players_profile(player_profile):
    """
    Evaluate each player's profile
    and display once all players finishes their turns
    """
    for i in player_profile.keys():
        player_bet = player_profile[i][0]
        player_score = player_profile[i][1]
        if player_score > 21:
            player_profile[i].append("BUSTED")
        elif player_score <= 21:
            player_profile[i].append("PLAYING")
