def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

# Input from user
text = input("Enter a string: ")

if palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")