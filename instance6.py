# Create an instance of the TextFileReader class
reader = usertest("test.txt")  # Replace with your file path

# Read the file content
reader.read_file()

# Display the content of the file
print("File Content:")
reader.display_content()

# Display statistics about the file
print("\nStatistics:")
print(f"Total Lines: {reader.count_lines()}")
print(f"Total Words: {reader.count_words()}")
print(f"Total Characters: {reader.count_characters()}")