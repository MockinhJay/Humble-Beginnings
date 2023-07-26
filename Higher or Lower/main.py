from art import logo 
from art import vs
from gameData import data
import random
from clearFunction import clear

score = 0
keep_playing = False

def select_question_set():
    """Returns the question set for A and B"""
    global dicA
    global dicB
    dicA = random.choice(data)
    dicB = random.choice(data)
    return f"Compare A: {dicA['name']}, {dicA['description']}, from {dicA['country']}\n{vs}\nAgainst B: {dicB['name']}, {dicB['description']}, from {dicB['country']}"

def is_correct(choice, dicA, dicB):
    if choice == "A":
        followers = int(dicA["follower_count"])
        if followers < int(dicB["follower_count"]):
            return False
        else:
            return True

    elif choice == "B":
        followers = int(dicB["follower_count"])
        if followers < int(dicA["follower_count"]):
            return False
        else:
            return True
    
    
play_game = input("Type 'y' to play: ")

if play_game == "y":
    keep_playing = True

while keep_playing:
    clear()
    print(logo)
    if score > 0:
        print(f"You are right! Current Score: {score}")
    print(select_question_set())
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if is_correct(choice, dicA, dicB):
        print("yay")
        score += 1
    else:
        keep_playing = False
        clear()
        print(f"Sorry that's wrong. Your final score is {score}")
        play_again = input("Do you want to play again? Type 'y' or 'n': ")
        if play_again == "y":
            keep_playing = True
            score = 0
        else:
            keep_playing = False
        

