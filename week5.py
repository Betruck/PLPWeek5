# File Creation
try:
    with open("my_file.txt", 'w') as file:
        file.write("First line: Hello, World!\n")
        file.write("Second line: PLP teaches you alot\n")
        file.write("Third line: Not only file handling\n")
    print("File created and initial content written successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error creating file: {e}")

# File Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nContents of the file:")
        print(content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error reading file: {e}")

# File Appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("Fourth line: It has been a great journey.\n")
        file.write("Fifth line: Not that it is over.\n")
        file.write("Sixth line: Great module indeed.\n")
    print("\nAdditional lines appended successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error appending to file: {e}")

# Final clean-up or closing tasks if needed
finally:
    print("\nFile handling operations are complete.")
