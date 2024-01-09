import json

# Python data structure (dictionary)
python_data = {
    "name": "John",
    "age": 25,
    "city": "Example City"
}

# Convert Python data structure to JSON string
json_string = json.dumps(python_data)

# Print the resulting JSON string
print(json_string)

