while True:
    number = int(input("Enter the number of visitors (max 9): "))
    if number <= 9:
        break
    print("Too many people!")

stop_counter = 0
while stop_counter != number:
    visitor = input("Enter name: ")
    stop_counter += 1
    print(f"{visitor} has been invited. {stop_counter}")
else:
    print("Ready!")
