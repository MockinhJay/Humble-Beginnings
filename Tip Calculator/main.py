print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill?\n"))
tipPercentage = int(input("What percentage tip would you like to give? 5, 10, 12, 15?\n"))
people = int(input("How many people are splitting the bill?\n"))

total = bill * (100 + tipPercentage)/100

paymentForEachPerson = total/people
#finalAmount = round(paymentForEachPerson, 2)
finalAmount = "{:.2f}".format(paymentForEachPerson)

print(f"Each person should pay: {finalAmount}")