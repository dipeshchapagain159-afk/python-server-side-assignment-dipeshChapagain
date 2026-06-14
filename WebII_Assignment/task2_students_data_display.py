#Create a program that takes a list of student names and stores them in a file.Then,read the file and display the contents.

#Ask the user for total number of student
num = int(input("Enter the number to students to store their name: "))

#Opening file in write mode
with open("student.txt","w") as file:
    file.write(f"Name of {num} students: \n")
    for i in range(num):
        name = input(f"Enter the name of Student {i+1}: ")
        file.write(f"{i+1}: {name}\n")

with open("student.txt","r") as file:
    for line in file:
        print(line.strip())