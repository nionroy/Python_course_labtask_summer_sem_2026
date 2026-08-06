try:
    # Create a file and write data
    file = open("student.txt", "w")
    file.write("Name: John\n")
    file.write("Department: CSE\n")
    file.close()

    print("File created and data written successfully.")

    # Read the file
    file = open("student.txt", "r")
    print("\nFile Content:")
    print(file.read())
    file.close()

    # Append new data
    file = open("student.txt", "a")
    file.write("Semester: 3rd\n")
    file.close()

    print("\nNew data appended successfully.")

    # Read the updated file
    file = open("student.txt", "r")
    print("\nUpdated File Content:")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("An unexpected error occurred:", e)