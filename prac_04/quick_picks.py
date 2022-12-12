import random

MIN_PICK= 1
MAX_PICK= 45
LENGTH= 6

quick_pick_amount= int(input("How many quick picks? "))

for i in range(quick_pick_amount):
    picks = []
    for i in range (LENGTH):
        pick= random.randint(MIN_PICK, MAX_PICK)
        while pick in picks:
            pick = random.randint(MIN_PICK, MAX_PICK)
        picks.append(pick)
    picks.sort()
    print(" ".join(f"{pick:2}" for pick in picks))
