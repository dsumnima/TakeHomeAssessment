'''
Program: Perform basic NumPy operations on an array
'''

import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50])

# Operations
total_sum = np.sum(arr)
mean_value = np.mean(arr)
max_value = np.max(arr)
min_value = np.min(arr)

# Display results
print("Array:", arr)
print("Sum:", total_sum)
print("Mean:", mean_value)
print("Maximum:", max_value)
print("Minimum:", min_value)
