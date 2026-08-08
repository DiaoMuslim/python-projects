import random
print("=== Number Guessing Game ===")
secret_number = random.randint(1, 10)
attempt = 1
guess=int(input("Guess a number between 1 and 10:"))
while guess != secret_number:
    if guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again")
    attempt +=1
    guess = int(input("Guess again:"))

print("You guessed the number in", attempt, "attempt(s).")        