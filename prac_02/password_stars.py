password=input("Enter your password: ")
while len(password)< 5:
    print("Too short")
    password = input("Enter your password: ")
print(len(password)* "*")