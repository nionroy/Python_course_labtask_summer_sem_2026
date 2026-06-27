# Lambda function to check if a string starts with a given substring
starts_with = lambda string, sub: string.startswith(sub)

# Input from user
text = input("Enter a string: ")
substring = input("Enter the substring: ")

# Check and display result
if starts_with(text, substring):
    print("The string starts with the given substring.")
else:
    print("The string does not start with the given substring.")