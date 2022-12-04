
number_list= []
rounds= 5
for i in range(rounds):
    number=int(input("Number: "))
    number_list.append(number)

print(f"The first number is {number_list[0]}")
print(f"The last number is {number_list[-1]}")
print(f"The smallest number is {min(number_list)}")
print(f"The largest number is {max(number_list)}")
total_number_list=sum(number_list)
average_number= total_number_list/rounds
print(f"The average numbers is {average_number}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username=input("Enter your username: ")
if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")