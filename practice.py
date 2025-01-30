# Demonstrating Python Variables and Functions

# Defining variables
name = "Alice"
age = 25
is_student = True
grades = [85, 90, 78, 92]  

# Function to greet a user
def greet_user(username):
    """
    Function to greet the user.
    Args:
        username (str): The name of the user.
    Returns:
        str: A greeting message.
    """
    return f"Hello, {username}! Welcome to Python practice."

# Function to calculate the average grade
def calculate_average(grades):
    """
    Function to calculate the average of a list of grades.
    Args:
        grades (list): A list of numerical grades.
    Returns:
        float: The average grade.
    """
    return sum(grades) / len(grades) if grades else 0

# Function to check if a user is eligible for a discount
def check_discount(age, student_status):
    """
    Function to check discount eligibility.
    Args:
        age (int): Age of the user.
        student_status (bool): Whether the user is a student.
    Returns:
        str: Discount eligibility message.
    """
    if age < 18 or student_status:
        return "You are eligible for a discount!"
    else:
        return "Sorry, no discount available."

# Function demonstrating loops and conditionals
def check_passing_status(grades):
    """
    Function to check if a student passes based on grades.
    Args:
        grades (list): A list of grades.
    Returns:
        str: Pass or fail message.
    """
    average = calculate_average(grades)
    return "You passed!" if average >= 60 else "You failed."

# Main block to execute functions
if __name__ == "__main__":
    # Greet the user
    print(greet_user(name))

    # Calculate and display average grade
    average_grade = calculate_average(grades)
    print(f"Your average grade is: {average_grade:.2f}")

    # Check discount eligibility
    discount_message = check_discount(age, is_student)
    print(discount_message)

    # Check if the student passed
    pass_status = check_passing_status(grades)
    print(pass_status)
