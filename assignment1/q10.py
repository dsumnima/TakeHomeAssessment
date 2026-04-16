import random

secret = random.randint(1, 50)

for i in range(1, 8):
    guess = int(input(f"Attempt {i}: Enter your guess: "))

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct!")
        break
else:
    print("Better luck next time!")
    print("Number was:", secret)
