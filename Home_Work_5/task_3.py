compnum = 50
attempts = 0
guess = int(input("Enter a number: "))
while guess != compnum:
    attempts += 1
    if guess < compnum:
        print("Your guess is lower(<).")
    else:
        print("Your guess is higher(>).")
    guess = int(input("Enter another number: "))
print(f"Well done, your attempts - {attempts}.")
