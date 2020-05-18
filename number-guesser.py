import random

number = random.randint(1, 101)
guessed = False
print(f"(Pre-game) The starting number is: {number}")
user_num = input("Guess a number between 1 and 100 (inclusive):\n")
while not guessed:
    try:
        user_num = int(user_num)
    except ValueError:
        print("That is not a valid number. Try again")
        continue
    
    if user_num == number:
        print(f"You guessed it! The number was {user_num}")
        exit(1)
    else:
        if user_num < number:
            print("Wrong. Higher")
        else:
            print("Wrong. Lower.")

    user_num = input(">")

