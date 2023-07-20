import random
from hangmanArt import stages
from hangmanWords import wordList
from hangmanArt import logo

end_of_game = False
lives = 6

def addLetter(blankWord):
  for char in blankList:
    blankWord += char
  print(blankWord)
  
#Create Blanks
blankList = []
blankWord = ""
choosenWord = random.choice(wordList)
#print(f"Pssst, the word is {choosenWord}")
print(logo)
print(stages[6])

for _ in range(len(choosenWord)):
  blankList.append("_ ")
  
addLetter(blankWord)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in blankList:
      print(f"You have already guessed {guess}, try another word")
  
  #replacing blank with the letter
    for position in range(len(choosenWord)):
        letter = choosenWord[position]
        if letter == guess:
            blankList[position] = letter
        
    if guess not in choosenWord:
      lives -= 1
      print(stages[lives])
      print(f"Oops! Letter did not match. You have {lives} lives left")
      if lives == 0:
        end_of_game = True
        print(f"You Loose, the word was {choosenWord}")
      
    addLetter(blankWord)
    
    #print(blankList)

    if "_ " not in blankList:
      end_of_game = True
      print("You Win")
  
  

  
