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
    input_data = [1, 1, 1, 1, 1]  # Тут можно инпут, но я сразу для теста так сделал
    print(calculate_points(input_data))
