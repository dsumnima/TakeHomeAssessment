def count_occurrences(lst):
    result = {}
    for num in lst:
        result[num] = result.get(num, 0) + 1
    return result

# Testing
print(count_occurrences([1,2,2,3,3,3]))
print(count_occurrences([4,4,4,4]))
print(count_occurrences([5,6,7]))
