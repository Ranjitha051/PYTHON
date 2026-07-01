# Write lines to file.
file_path = "my_file.txt"
content_to_write = "Hello, Python!\nThis is a new line."
content_to_overwrite = "This is the new content."
content_to_append = "This is the appended content."

# Open a file in write mode
with open(file_path, 'w') as file:
    file.write(content_to_write)
    print(f"Content written to '{file_path}'.")

# Open a file in read mode
with open(file_path, "r") as file:
    content = file.read()
    print(f"Content read from '{file_path}':\n{content}")
