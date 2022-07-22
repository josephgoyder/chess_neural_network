import random


def p(wins, losses, win_odds):
    s = 0
    for x in range(2000):
        w = 0
        for y in range(wins + losses):
            w += int(random.uniform(0, 1) <= win_odds)
        s += int(w >= wins)
    print(f"p: {s/2000}")

