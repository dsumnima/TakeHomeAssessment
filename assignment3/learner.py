'''
Program: Create Learner class and display details
'''

class Learner:
    def __init__(self, roll_no, full_name, address, year, program, group):
        self.roll_no = roll_no
        self.full_name = full_name
        self.address = address
        self.year = year
        self.program = program
        self.group = group

    def display(self):
        print("\n--- Learner Details ---")
        print("Roll No:", self.roll_no)
        print("Name:", self.full_name)
        print("Address:", self.address)
        print("Year:", self.year)
        print("Program:", self.program)
        print("Group:", self.group)

# Input from user
learner = Learner(
    input("Enter Roll No: "),
    input("Enter Full Name: "),
    input("Enter Address: "),
    input("Enter Year: "),
    input("Enter Program: "),
    input("Enter Group: ")
)

learner.display()
