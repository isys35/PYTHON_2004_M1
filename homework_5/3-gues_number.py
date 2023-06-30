# Homework-5: Task-3
"""
Создайте переменную с именем comp_num и присвойте ей значение 50. Предложите пользователю ввести число.
Пока предположение не совпадает со значением comp_num, сообщите, больше оно или меньше comp_num,
и предложите ввести другое число. Если введенное значение совпадет с comp_num, выведите сообщение «Well done,
you took [попытки] attempts».
"""

comp_num = 50
attempts = 0
guess = int(input("Enter a number: "))
while guess != comp_num:
    attempts += 1
    if guess < comp_num:
        print("Your guess is lower(<).")
    else:
        print("Your guess is higher(>).")
    guess = int(input("Enter another number: "))
print(f"Well done, your attempts - {attempts}.")
