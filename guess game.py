import random

num = random.randint(1, 20)
print("Guess a number between 1 and 20")

for i in range(6):
    guess = int(input("Your guess: "))
    if guess == num:
        print("You guessed it!")
        break
    elif guess < num:
        print("Too low")
    else:
        print("Too high")
else:
    print("Out of tries! The number was", num)
