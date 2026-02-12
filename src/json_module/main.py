import json

# data = {"name": "Abdullah", "age": 21}
# print(data)
# json_string = json.dumps(data)  # Convert Python dict to JSON string
# print(json_string)  # Output: '{"name": "Abdullah", "age": 21}'


# json_string = '{"name": "Abdullah", "age": 21}'
# print(json_string)
# python_data = json.loads(json_string)  # Convert JSON string to Python dict
# print(python_data)  # Output: Abdullah


# import json

new_data = {"name": "Abdullah", "age": 21, "city": "Karachi"}
try:
    with open("json/data.json", "r") as file:
        data = json.load(file)
        if not isinstance(data, list):  # Ensure data is a list
            data = [data]  
except (FileNotFoundError, json.JSONDecodeError):
    data = []

data.append(new_data)
with open("json/data.json", "w") as file:
    json.dump(data, file, indent=4)  # `indent=4` makes it look pretty
