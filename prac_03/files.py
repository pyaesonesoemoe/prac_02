#1
name= input("Enter your name: ")
out_file=open("name.txt", "w")
print(name, file= out_file)
out_file.close()

#2
in_file=open("name.txt", "r")
name=in_file.read()
in_file.close()

print(f"Your name is {name}")

#3
in_file=open("numbers.txt", "r")
first_num=int(in_file.readline())
second_num=int(in_file.readline())
in_file.close()
print(first_num + second_num)

#4
num_file=open("numbers.txt", "r")
