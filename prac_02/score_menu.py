def main():
    MENU="""(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    print(MENU)
    option=input("Enter your option: ").lower
    while option != "q":
        if option == "g":
            score = float(input("Enter score: "))
            check=check_status(score)
            while check == "Invalid score":
                print("Invalid score")
                score = float(input("Enter score: "))
        elif option == "p":
            score = float(input("Enter score: "))
            check = check_status(score)
        elif option == "s":
            score = int(input("Enter score: "))
            if score> 0:
                print("*" * int(score))
            else:
                print("Invalid score")
                score = int(input("Enter score: "))
        else:
            print("Option is invalid")
        print(MENU)
        option = input("Enter your option: ").lower
    else:
        print("Farewell")


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