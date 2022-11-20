

def main():
    score = float(input("Enter score: "))
    print(check_status(score))

def check_status(score):
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
main()