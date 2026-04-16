def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "Division by zero"

def floor_division(a, b):
    return a // b if b != 0 else "Division by zero"

def exponentiation(a, b):
    return a ** b

# Example
a, b = 10, 3
print("Addition:", addition(a, b))
print("Multiplication:", multiplication(a, b))
print("Division:", division(a, b))
print("Floor Division:", floor_division(a, b))
print("Exponentiation:", exponentiation(a, b))
