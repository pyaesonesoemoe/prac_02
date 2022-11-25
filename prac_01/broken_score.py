"""
CP1404/CP5632 - Practical
Broken program to determine score status
get score
while 0 <= score <=100
     if score <90
        display Excellent
    else if score >= 50
        display Passable
    else
        display Bad
    get score
else
    display Invalid Score
"""

# TODO: Fix this!

score = float(input("Enter score: "))
while 0<= score <= 100:
        if score>90:
            print("Excellent")
        elif score>=50:
            print("Passable")
        else:
            print("Bad")
        score = float(input("Enter score: "))
else:
    print("Invalid score")
