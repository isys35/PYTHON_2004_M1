# Homework-8: Task-1
"""
Greed is a dice game played with five six-sided dice.
Your mission, should you choose to accept it, is to score a throw according to these rules.
You will always be given an array with five six-sided dice values.
https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python
"""

import random

SCORES = {
    (1, 3): 1000,
    (6, 3): 600,
    (5, 3): 500,
    (4, 3): 400,
    (3, 3): 300,
    (2, 3): 200,
    (1, 1): 100,
    (5, 1): 50
}


def calculate_points(dice):
    base_dice = dict()
    for elem in set(dice):
        base_dice[elem] = dice.count(elem)

    points = 0
    count = len(dice)
    while count:
        for key in SCORES:
            if key[0] in base_dice:
                if key[1] <= base_dice.get(key[0]):
                    points += SCORES.get(key)
                    base_dice[key[0]] = base_dice.get(key[0]) - key[1]
        count -= 1

    return points


if __name__ == "__main__":

    throw = [random.randint(1, 6) for _ in range(5)]

    print(f"You throw: {throw}")
    print(calculate_points(throw))
