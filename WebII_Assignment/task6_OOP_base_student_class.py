class Studnet:
    def input_data(self):
        self.name = input("Enter Name: ")
        self.roll_num = int(input("Enter Roll_number: "))
        self.marks = float(input("Enter Marks: "))
    
    def displaying(self):
        print("\n----------Student Details----------")
        print("\tName: ",self.name)
        print("\tRoll_Number: ",self.roll_num)
        print("\tMarks: ",self.marks)
        print("\n")

s1 = Studnet()
s1.input_data()
s1.displaying()