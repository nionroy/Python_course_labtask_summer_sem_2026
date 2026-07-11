# Take input from the user
text = input("Enter a string: ")

# Reverse the string
reverse_text = text[::-1]

# Check if both strings are the same
if text == reverse_text:
    print("Palindrome")
else:
    print("Not a palindrome")