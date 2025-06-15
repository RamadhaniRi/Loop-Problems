import random

print("Guess a number between 1-100")

number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number: "))

    if guess > number:
        print("too high!")
        continue
    elif guess < number:
        print("too low!")
        continue
    else:
        print("You got it!")
        break

print("Yes the number is", number)