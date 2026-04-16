import random

def dice_game():
    dice = random.randint(1, 6)
    guess = int(input("Guess the dice value (1-6): "))

    print("Dice value:", dice)

    if guess == dice:
        print("😊 Correct Guess!")
    elif abs(guess - dice) == 1:
        print("😐 Close Guess!")
    else:
        print("😞 Wrong Guess!")

# Run game
dice_game()
