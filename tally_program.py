from operator import itemgetter
# Tally Program Challenge:
# 5 Friends let's call them a, b, c, d and e)
# are playing a game and need to keep track of the scores.
# Each time someone scores a point, the letter of his name
# is typed in lowercase. If someone loses a point, the letter
# of his name is typed in uppercase. Give the resulting score
# from highest to lowest.
# Author: isaacsutor
# Version: 2018912

# Test String: EbAAdbBEaBaaBBdAccbeebaec
# Solution: c : 3, d : 2, a : 1, e : 1, b : 0


def tally_up(score_str):
    scoreboard = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
    for letter in score_str:
        if letter.lower() in scoreboard:
            for person in scoreboard:
                if letter == person:
                    scoreboard[person] += 1
                elif letter.lower() == person:
                    scoreboard[person] -= 1
    score = sorted(scoreboard.items(), key=itemgetter(1), reverse=True)
    print(score)


tally_up("EbAAdbBEaBaaBBdAccbeebaec")


