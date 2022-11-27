import random

print(random.randint(5,20))  # line 1
print(random.randrange(3,10,2)) # Line 2
print(random.uniform(2.5,5.5)) # Line 3

"""What did you see on line 1?
Random number between 5 and 20 is displayed
What was the smallest number you could have seen, what was the largest?
5 and 20

What did you see on line 2?
Random number between 3 and 10 with differences of 2 is displayed
What was the smallest number you could have seen, what was the largest?
3 and 9
Could line 2 have produced a 4?
No, it couldn't

What did you see on line 3?
Random decimal between 2.5 and 5.5 is displayed
What was the smallest number you could have seen, what was the largest?
2.5 and 5.4
"""

print(random.randint(1, 100))