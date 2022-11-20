def main():
    password= get_password()
    show_asterisks(password)

def get_password():
    password = input("Enter your password: ")
    while len(password) < 5:
        print("Too short> Please enter again.")
        password= input("Enter your password: ")
    return password

def show_asterisks(keywords):
    print(len(keywords) * "*")

main()

