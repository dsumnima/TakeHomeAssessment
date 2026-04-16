marks = []

for i in range(6):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

total = sum(marks)
average = total / 6
percentage = (total / 600) * 100

print("Total:", total)
print("Average:", average)
print("Percentage:", percentage)

if percentage >= 85:
    print("Grade: Distinction")
elif percentage >= 70:
    print("Grade: First Division")
elif percentage >= 55:
    print("Grade: Second Division")
elif percentage >= 45:
    print("Grade: Third Division")
else:
    print("Grade: Fail")
