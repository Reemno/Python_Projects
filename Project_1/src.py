import random


def user_guess(min_number, max_number):
    random_number = random.randint(min_number, max_number)
    user_number = None
    print(f"Guess the number between {min_number} and {max_number}")
    while user_number != random_number:
        user_number = int(input())
        if user_number > random_number:
            print("Wrong! The number is lower")
        elif user_number < random_number:
            print("Wrong! The number is higher")
    print(f"Correct! You have guessed the correct number ({random_number})!")


def computer_guess(min_number, max_number):
    random_number = random.randint(min_number, max_number)
    computer_number = None
    while computer_number != random_number:
        computer_number = random.randint(min_number, max_number)
        print(f"My guess is {computer_number}")
        if computer_number > random_number:
            print("Wrong! The number is lower")
            max_number = computer_number - 1
        elif computer_number < random_number:
            print("Wrong! The number is higher")
            min_number = computer_number + 1
    print(f"Correct! You have guessed the correct number ({random_number})!")


# choose one of the mods
# user_guess(int(input("Choose minimal number")),int(input("Choose maximal number")))
# computer_guess(int(input("Choose minimal number")), int(input("Choose maximal number")))
