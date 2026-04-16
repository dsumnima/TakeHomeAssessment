'''
Program: Generate random NumPy array, sort and reshape it
'''

import numpy as np

# Generate random array of 12 elements
arr = np.random.randint(1, 100, 12)

print("Original Array:", arr)

# Sort array
sorted_arr = np.sort(arr)
print("Sorted Array:", sorted_arr)

# Reshape (3x4 matrix)
reshaped = sorted_arr.reshape(3, 4)

print("Reshaped Matrix (3x4):\n", reshaped)
