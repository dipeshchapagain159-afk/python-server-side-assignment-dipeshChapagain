#Implement a program to store student records (name,roll,marks,contact number) using a dictionary.
    #a. Provide menu option to add, search and display studnets.

#creating dictionary
students_record = {}

while True:
    print("\n\tStudent Records\n")
    print("1.Add the student Record: ")
    print("2.Search the student Record: ")
    print("3.Display Records: ")
    print("4.Exit\n")

    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Please enter number:")
        continue

    if(choice==1):
        name = input("Enter the name of student: ")
        try:
            roll = int(input("Enter roll_no:"))
            marks = float(input("Enter marks "))
        except ValueError:
            print("Invalid input for roll_no and marks")
            continue
        contact = input("Enter the contact info: +977-")

        students_record[roll]={
            "name":name,
            "marks":marks,
            "contact":contact
        }
        print("Student Info added Successfully")
    elif(choice==2):
        try:
            roll = int(input("Enter roll_no of entended student: "))
        except ValueError:
            print("Invalid Roll_number:")
            continue

        if roll in students_record:
            print("Student Found")
            print(f"Name: {students_record[roll]['name']}")
            print(f"Marks: {students_record[roll]['marks']}")
            print(f"Contact: {students_record[roll]['contact']}")
        else:
            print("Student Not Found")

    elif choice ==3:
        if not students_record:
            print("Student Record Unavailable")
        else:
            print("Student Record")
            for roll, details in students_record.items():
                print("Roll: ",roll)
                print("Name: ",name)
                print("Marks: ",marks)
                print("Contact: ",contact)
                print("\n")
    elif choice == 4:
        print("Exit")
        break
    else:
        print("Wrong Input")