positive_sum = 0
negative_sum = 0

while True:
    print("\n1. Enter number")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        num = float(input("Enter number: "))
        if num >= 0:
            positive_sum += num
        else:
            negative_sum += num

    elif choice == "2":
        break
    else:
        print("Invalid choice")

print("Sum of positive numbers:", positive_sum)
print("Sum of negative numbers:", negative_sum)
