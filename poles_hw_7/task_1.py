FAT_COEFFICIENT = 9
СH_COEFFICIENT = 4

def fat_calculation (input_1):
    print(f'Количество полученных каллорий от жиров в граммах: {input_1 * FAT_COEFFICIENT}')


def ch_calculation(input_2):
    print(f'Количество полученных каллорий от углеводов в граммах: {input_2 * СH_COEFFICIENT}')

if __name__ == '__main__':

    user_input_1 = float(input('Введите количество употребленных жиров:'))
    user_input_2 = float(input('Введите количество употребленных углеводов:'))

print(fat_calculation(user_input_1))
print(ch_calculation(user_input_2))







