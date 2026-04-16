'''
Program: Manage staff records and store in staff.csv
'''

import csv

class Staff:
    def __init__(self, emp_id, name, address, phone, status, dependents, salary):
        self.emp_id = emp_id
        self.name = name
        self.address = address
        self.phone = phone
        self.status = status
        self.dependents = dependents
        self.salary = salary

def add_staff():
    try:
        with open("staff.csv", "a", newline="") as file:
            writer = csv.writer(file)

            n = int(input("Enter number of staff: "))
            for _ in range(n):
                staff = Staff(
                    input("ID: "),
                    input("Name: "),
                    input("Address: "),
                    input("Phone: "),
                    input("Marital Status: "),
                    input("Dependents: "),
                    input("Salary: ")
                )
                writer.writerow(vars(staff))

    except Exception as e:
        print("Error:", e)

def view_staff():
    try:
        with open("staff.csv", "r") as file:
            reader = csv.reader(file)
            print("\n--- Staff Records ---\n")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No staff file found.")

add_staff()
view_staff()
