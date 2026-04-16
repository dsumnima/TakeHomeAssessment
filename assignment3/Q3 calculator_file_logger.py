'''
Program: Perform operations and store results with date and time
'''

from datetime import datetime

def calculator():
    filename = "results.txt"

    while True:
        try:
            nums = list(map(int, input("Enter two numbers: ").split()))
            if len(nums) < 2:
                print("Please enter at least two numbers.")
                continue

            a, b = nums[0], nums[1]

            add = a + b
            sub = a - b
            mul = a * b
            div = a / b if b != 0 else "Undefined"

            with open(filename, "a") as file:
                file.write(f"\nDate & Time: {datetime.now()}\n")
                file.write(f"Addition: {add}\n")
                file.write(f"Subtraction: {sub}\n")
                file.write(f"Multiplication: {mul}\n")
                file.write(f"Division: {div}\n")

            choice = input("Continue? (y/n): ")
            if choice.lower() != 'y':
                break

        except ValueError:
            print("Invalid input!")

    print("\n--- File Contents ---\n")
    with open(filename, "r") as file:
        print(file.read())

calculator()
