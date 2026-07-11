# Given list
words = ['aca', 'xyz', 'aba', '1221']

count = 0

# Check each word
for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count = count + 1

# Print the result
print("Number of matching strings:", count)