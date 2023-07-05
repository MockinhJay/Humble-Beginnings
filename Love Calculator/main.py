print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()


T1 = name1.count("t")
T2 = name2.count("t")
T = T1 + T2

R1 = name1.count("r")
R2 = name2.count("r")
R = R1 + R2

U1 = name1.count("u")
U2 = name2.count("u")
U = U1 + U2

E1 = name1.count("e")
E2 = name2.count("e")
E = E1 + E2

trueTotal = T + R + U + E

L1 = name1.count("l")
L2 = name2.count("l")
L = L1 + L2

O1 = name1.count("o")
O2 = name2.count("o")
O = O1 + O2

V1 = name1.count("v")
V2 = name2.count("v")
V = V1 + V2

E1 = name1.count("e")
E2 = name2.count("e")
E = E1 + E2

loveTotal = L + O + V + E

score = trueTotal*10 + loveTotal

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}")