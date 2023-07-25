import random

keep_guessing = True

picked_number = random.randint(1, 101)
print(f"Picked number is {picked_number}")

print("Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    guess_attempts = 10
elif difficulty == "hard":
    guess_attempts = 5

while keep_guessing:
    print(f"You have {guess_attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    guess_attempts -= 1
    if guess_attempts == 0:
        keep_guessing = False
        print("You failed to guess the number")
    elif guess > picked_number:
        print("Too High")
        print("Guess again.")
    elif guess < picked_number:
        print("Too Low")
        print("Guess again.")
    elif guess == picked_number:
        print(f"You guessed correctly! The number is {picked_number}")






