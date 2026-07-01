marks = [78, 85, 92, 67, 88]


maximum = max(marks)
minimum = min(marks)

print("Maximum Marks:", maximum)
print("Minimum Marks:", minimum)


students = ["Alice", "Bob", "Charlie", "David", "Emma"]
marks = [78, 85, 92, 67, 88]

combined = list(zip(students, marks))

print("\nStudent Names and Marks:")
for name, mark in combined:
print(name, ":", mark)
