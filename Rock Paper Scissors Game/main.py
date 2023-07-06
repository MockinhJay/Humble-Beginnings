import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


computerHand = [rock, paper, scissors]
choiceHand = [rock, paper, scissors]

choiceID = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
choice = choiceHand[choiceID]
print(choice)
computerChoice = computerHand[random.randint(0, 2)]
print(f"The computer chose: {computerChoice}")

if choice == rock and computerChoice == rock:
  print("Draw")

elif choice == rock and computerChoice == paper:
  print("You Loose")

elif choice == rock and computerChoice == scissors:
  print("You Win")

elif choice == paper and computerChoice == rock:
  print("You Win")

elif choice == paper and computerChoice == paper:
  print("Draw")

elif choice == paper and computerChoice == scissors:
  print("You Loose")

elif choice == scissors and computerChoice == rock:
  print("You Loose")

elif choice == scissors and computerChoice == paper:
  print("You Win")

elif choice == scissors and computerChoice == scissors:
  print("You Draw")