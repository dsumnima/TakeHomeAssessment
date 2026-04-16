'''
Program: Read records.csv and display its contents
'''

import csv

# Function to read and display records
def read_records():
    try:
        with open("Q1 read_records.csv", "r") as file:
            reader = csv.reader(file)
            print("\n--- Student Records ---\n")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Error: records.csv file not found.")

# Run function
read_records()
