def key_value(sentence):
    result = {}
    for char in sentence:
        if char != " ":
            result[char] = result.get(char, 0) + 1
    return result

# Example
print(key_value("hello world"))
