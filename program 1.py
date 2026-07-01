# List of marks
marks = [78, 85, 92, 67, 88]

# Find maximum and minimum values
maximum = max(marks)
minimum = min(marks)

print("Maximum Marks:", maximum)
print("Minimum Marks:", minimum)

# Lists of student names and marks
students = ["Alice", "Bob", "Charlie", "David", "Emma"]
marks = [78, 85, 92, 67, 88]

# Combine lists using zip()
combined = list(zip(students, marks))

# Display the combined result
print("\nStudent Names and Marks:")
for name, mark in combined:
    print(name, ":", mark)
