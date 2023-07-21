from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  endText = ""
  if direction == "decode":
      shift *= -1
  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      newPosition = position + shift
      newLetter = alphabet[newPosition]
      endText += newLetter
    else:
      endText += char
  print(f"The {direction}d word is {endText}")

print(logo)

shouldContinue = True

while shouldContinue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shit = shift % 26
      
  caesar(text = text, shift = shift, direction = direction)

  result = input('Type "yes" if you want to go again. Otherwise type "no".\n')
  if result == "no":
    shouldContinue = False
    print("Goodbye")