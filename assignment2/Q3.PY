def is_armstrong(num_str):
    num = int(num_str)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)

    if total == num:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is NOT an Armstrong number")

# Example
is_armstrong("153")
