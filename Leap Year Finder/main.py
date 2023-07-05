year = int(input("Which year do you want to check? "))

testOne = year % 4
testTwo = year % 100
testThree = year % 5

if testOne == 0:
    if testTwo != 0:
        print("Leap Year.")
    if testTwo == 0:
        if testThree == 0:
            print("Leap year.")
        if testThree !=0:
            print("Not leap year.")

if testOne != 0:
    print("Not leap year.")