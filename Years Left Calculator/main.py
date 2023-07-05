age = input("What is your current age? ")

yearsLeft = 90 - int(age)
monthsLeft = yearsLeft * 12
weeksLeft = yearsLeft * 52
daysLeft = yearsLeft * 365

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.\n")