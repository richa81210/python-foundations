import random
secret = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")

i = 0
while True:
    guess = int(input("Enter your guess (0 to quit):"))
    if guess == 0:
        print(f"You quit the game. The number was {secret}.")
        break
    i +=1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You got it in {i} guesses!")
        break