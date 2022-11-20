def main():
    score = float(input("Enter score: "))
    print(check_status(score))



def check_status(score):
    while 0<= score <= 100:
        if score>90:
            return "Excellent"
        elif score>=50:
            return "Passable"
        else:
            return"Bad"
    else:
        return "Invalid score"
main()