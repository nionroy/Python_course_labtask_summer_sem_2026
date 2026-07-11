# Take input from the user
text = input("Enter a string: ")

# Split the string into words
words = text.split()

# Reverse each word
result = ""

for word in words:
    reverse_word = word[::-1]
    result = result + reverse_word + " "

# Print the final result
print("Reversed string:", result.strip())