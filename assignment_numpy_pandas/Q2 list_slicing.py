'''
Program: Take list input, sort it and perform slicing operations
'''

# Take input (at least 12 numbers)
numbers = list(map(int, input("Enter at least 12 numbers: ").split()))

# Sort list
numbers.sort()

print("Sorted List:", numbers)

# Slicing
print("Index 3–6:", numbers[3:7])
print("Index 6–9:", numbers[6:10])
print("Index 4–10:", numbers[4:11])
