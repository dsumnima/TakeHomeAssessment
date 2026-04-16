import csv

def append_record():
    try:
        file_name = "Q2 append_records.csv"
        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)

            name = input("Enter student name: ")
            roll = input("Enter roll number: ")
            program = input("Enter program: ")
            year = input("Enter year: ")
            group = input("Enter group: ")

            writer.writerow([name, roll, program, year, group])
            print("\nRecord added successfully!\n")

        # Show table after adding
        print("\n--- Updated Student Records ---\n")

        with open(file_name, "r") as file:
            reader = csv.reader(file)

            print(f"{'Name':20} {'Roll':6} {'Program':15} {'Year':6} {'Group':6}")
            print("-" * 60)

            for row in reader:
                print(f"{row[0]:20} {row[1]:6} {row[2]:15} {row[3]:6} {row[4]:6}")

    except Exception as e:
        print("Error:", e)

append_record()