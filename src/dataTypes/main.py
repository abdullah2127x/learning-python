# First, install required packages using:
# pip install requests

import requests
import json
from datetime import datetime

# 1. LISTS - ordered, mutable collection
# List operations and methods
fruits = ["apple", "banana", "orange", "mango"]
numbers = [1, 2, 3, 4, 5]

# List operations
fruits.append("grape")  # Add element at end
fruits.insert(1, "pineapple")  # Insert at specific position
fruits.remove("banana")  # Remove specific element
last_fruit = fruits.pop()  # Remove and return last element
fruits.sort()  # Sort list in place
fruits.reverse()  # Reverse list in place

# List comprehension
squares = [x**2 for x in range(1, 6)]
even_numbers = [x for x in numbers if x % 2 == 0]

print("\n=== List Operations ===")
print(f"Original fruits: {fruits}")
print(f"Squares: {squares}")
print(f"Even numbers: {even_numbers}")

# 2. TUPLES - ordered, immutable collection
# Tuple operations
coordinates = (10, 20, 30)
rgb_colors = ((255, 0, 0), (0, 255, 0), (0, 0, 255))
single_item_tuple = (1,)  # Note the comma

# Tuple unpacking
x, y, z = coordinates
red, green, blue = rgb_colors

print("\n=== Tuple Operations ===")
print(f"Coordinates: {coordinates}")
print(f"Unpacked coordinates: x={x}, y={y}, z={z}")
print(f"RGB Colors: {rgb_colors}")

# 3. DICTIONARIES - key-value pairs
# Dictionary creation and operations
student = {
    "name": "John Doe",
    "age": 20,
    "courses": ["Python", "Data Science", "Web Development"],
    "grades": {"Python": 95, "Data Science": 88, "Web Development": 92},
    "active": True,
}

# Dictionary methods
student["email"] = "john@example.com"  # Add new key-value pair
student.update({"phone": "123-456-7890"})  # Update multiple key-value pairs
courses = student.get("courses", [])  # Safe get with default value
student_keys = student.keys()  # Get all keys
student_values = student.values()  # Get all values
student_items = student.items()  # Get all key-value pairs

print("\n=== Dictionary Operations ===")
print(f"Student info: {json.dumps(student, indent=2)}")
print(f"Student keys: {student_keys}")

# 4. WORKING WITH REQUESTS
# Making HTTP requests to different APIs


def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        return response.json()
    except requests.RequestException as e:
        return f"Error fetching data: {e}"


# Example APIs to fetch data from
apis = {
    "users": "https://jsonplaceholder.typicode.com/users",
    "posts": "https://jsonplaceholder.typicode.com/posts",
    "todos": "https://jsonplaceholder.typicode.com/todos/1",
}

# Fetch and store data
api_data = {}
for api_name, url in apis.items():
    print(f"\nFetching {api_name} data...")
    data = fetch_data_from_api(url)
    api_data[api_name] = data

# 5. ADVANCED DATA STRUCTURE COMBINATIONS
# Combining lists, tuples, and dictionaries

# List of dictionaries
users = [
    {"id": 1, "name": "Alice", "skills": ("Python", "SQL")},
    {"id": 2, "name": "Bob", "skills": ("Java", "JavaScript")},
    {"id": 3, "name": "Charlie", "skills": ("Python", "React")},
]

# Dictionary of lists
department_employees = {
    "IT": ["Alice", "Bob", "Charlie"],
    "HR": ["David", "Eve"],
    "Finance": ["Frank", "Grace"],
}

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}

print("\n=== Advanced Data Structures ===")
print("Users with Python skills:")
python_users = [user["name"] for user in users if "Python" in user["skills"]]
print(python_users)

print("\nDepartment sizes:")
dept_sizes = {dept: len(employees) for dept, employees in department_employees.items()}
print(dept_sizes)


# 6. ERROR HANDLING AND DATA VALIDATION
def safe_get_user_data(users_list, user_id):
    try:
        return next((user for user in users_list if user["id"] == user_id), None)
    except Exception as e:
        return f"Error: {e}"


print("\n=== Error Handling Example ===")
user_data = safe_get_user_data(users, 1)
print(f"User data: {user_data}")

# Current timestamp
print("\n=== Script Information ===")
print(f"Script executed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def fetch_todo():
    """
    Fetch a single todo item from JSONPlaceholder API
    """
    # API endpoint for a single todo
    url = "https://jsonplaceholder.typicode.com/todos/1"

    try:
        # Make GET request
        print("Fetching data from:", url)
        response = requests.get(url)

        # Check if request was successful
        response.raise_for_status()

        # Get the JSON data
        todo_data = response.json()

        # Print the results in a formatted way
        print("\nTODO Item Details:")
        print(f"Title: {todo_data['title']}")
        print(f"Completed: {todo_data['completed']}")
        print(f"User ID: {todo_data['userId']}")

        # Print the full JSON response
        print("\nComplete JSON response:")
        print(json.dumps(todo_data, indent=2))

    except requests.RequestException as e:
        print(f"An error occurred: {str(e)}")


# Run the function
if __name__ == "__main__":
    fetch_todo()
