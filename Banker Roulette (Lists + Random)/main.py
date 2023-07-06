import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

listLenght = len(names)
randomNameId = random.randint(0, listLenght-1)
randomName = names[randomNameId]
print(f"{randomName} is going to buy the meal today!")