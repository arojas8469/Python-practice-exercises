# List and For Loop Example
fruits = ["Apple", "Banana", "Cherry", "Date"]

# Print each fruit using a for loop
for fruit in fruits:
    print(f"I love {fruit}")


# Dictionary Example
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Loop through dictionary keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# List of dictionaries
students = [
    {"name": "Alice", "age": 22, "grade": "A"},
    {"name": "Bob", "age": 24, "grade": "B"},
    {"name": "Charlie", "age": 23, "grade": "A"},
]

# Print student details
for student in students:
    print(f"{student['name']} is {student['age']} years old and got a {student['grade']}.")