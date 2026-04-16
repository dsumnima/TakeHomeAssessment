num = input("Enter a number: ")

if num.isdigit():
    num = int(num)
    if num >= 0:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        print("Factorial:", fact)
    else:
        print("Invalid input! Please enter a positive integer.")
else:
    print("Invalid input! Please enter a positive integer.")
