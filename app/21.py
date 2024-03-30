import random
import time
from utils import *
from scenarios import *

if __name__ == "__main__":

    deck = deck()
    fresh_deck = deck

    players_no = input_validation("players_no")
    round_no = input_validation("rounds_no")

    player_profile = {}

    if int(players_no) > 3:
        deck.extend(deck)

    round = 1
    while round <= round_no:
        header_line(f"Round {str(round)} starting in...")
        round += 1
        bet_split = 0

        for i in range(1, int(players_no) + 1):
            if i == 1:
                deck, bank_cards, bank_score, bet_val, score, bet_split = player(
                    deck, str(i)
                )
            else:
                deck, bank_cards, bank_score, bet_val, score, bet_split = player(
                    deck, str(i), bank_cards, bank_score
                )

            pp = []
            pp.append(bet_val)
            pp.append(score)
            player_profile[i] = pp

            if bet_split > 0:
                pp = []
                pp.append(bet_val)
                pp.append(bet_split)
                player_profile[str(i) + " Split 2"] = pp

            header_line(f"Player {str(i)} turn ended!")

        evaluate_players_profile(player_profile)
        header_line(f"Game Summary:")

        players_standing = 0
        for i in player_profile.keys():
            p_status = str(player_profile[i][2])
            p_bet = str(player_profile[i][0])
            p_score = str(player_profile[i][1])
            print(
                f"\nPlayer {str(i)}: Bet: {p_bet}, Score:{p_score}, Status:{p_status}"
            )

            if p_status == "PLAYING":
                players_standing += 1
        line()

        if players_standing > 0:
            bank_score = reveal_bank_cards(deck, str(i), bank_cards, bank_score)
            get_game_stats(player_profile, bank_score)
        else:
            print("All the players are Busted!")
            print("Bank is not revealing cards!")
            line()
        deck = fresh_deck

## THE END :)
