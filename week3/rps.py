# rock, paper, scissors

import random


def player1_turn():
    p1_choice = input(
        "Player 1, what do you choose?(1 for rock, 2 for paper, 3 for scissors): ")
    p1_choice = int(p1_choice)
    return p1_choice


def player2_turn():
    p2_choice = input(
        "Player 2, what do you choose?(1 for rock, 2 for paper, 3 for scissors): ")
    p2_choice = int(p2_choice)
    return p2_choice


def compare_choices(p1, p2):
    if p1 == 1 and p2 == 3:
        print("Player 1 won the round")
        return 1
    elif p1 == 1 and p2 == 2:
        print("Player 2 won the round")
        return 2
    elif p1 == 1 and p2 == 1:
        print("Ow shite dass a tie")
        return 3
    elif p1 == 2 and p2 == 1:
        print("Player 1 won the round")
        return 1
    elif p1 == 2 and p2 == 2:
        print("Ow shite dass a tie")
        return 3
    elif p1 == 2 and p2 == 3:
        print("Player 2 won the round")
        return 2
    elif p1 == 3 and p2 == 1:
        print("Player 2 won the round")
        return 2
    elif p1 == 3 and p2 == 2:
        print("Player 1 won the round")
        return 1
    elif p1 == 3 and p2 == 3:
        ("Ow shite dass a tie")
        return 3


def win_decider(ended_round, p1_wins, p2_wins, rounds):
    if rounds > 0:
        if ended_round == 1:
            p1_wins += 1
            return p1_wins
        if ended_round == 1:
            p2_wins += 1
            return p2_wins
        else:
            return


def main():
    rounds = input("How many rounds do you want to play?: ")
    rounds = int(rounds)
    win_state = 0
    p1_wins = 0
    p2_wins = 0
    while rounds >= 0:
        p1 = player1_turn()
        p2 = player2_turn()
        print(compare_choices(p1, p2))
        rounds -= 1
    if p1_wins > p2_wins:
        print("Player 1 won")
    if p2_wins > p1_wins:
        print("Player 2 won")
    else:
        print("Dass a Tie")


def main2():
    rounds = input("How many rounds do you want to play?: ")
    rounds = int(rounds)
    win_state = 0
    p1_wins = 0
    p2_wins = 0
    while rounds > 0:
        p1 = player1_turn()
        p2 = player2_turn()
        win_decider(compare_choices(p1, p2), p1_wins, p2_wins, rounds)
        rounds -= 1
    if p1_wins > p2_wins:
            print("Player 1 won")
    if p2_wins > p1_wins:
            print("Player 2 won")
    else:
            print("Dass a Tie")

main2()
