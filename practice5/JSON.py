import json

json_data = '{"name": "Alice", "age": 25}'
print(json_data)

json_array = '[1, 2, 3, 4, 5]'
print(json_array)

nested_json = '{"person": {"name": "Bob", "age": 30}, "city": "New York"}'
print(nested_json)


json_data = '{"name": "Alice", "age": 25}'
data = json.loads(json_data)
print(data['name'])
print(data['age'])


json_array = '[1, 2, 3, 4]'
numbers = json.loads(json_array)
print(numbers[2])


nested_json = '{"person": {"name": "Bob", "age": 30}, "city": "NY"}'
data = json.loads(nested_json)
print(data['person']['name'])
print(data['city'])


data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)
print(json_string)


numbers = [1, 2, 3, 4]
json_string = json.dumps(numbers)
print(json_string)


data = {"person": {"name": "Bob", "age": 30}, "city": "NY"}
json_string = json.dumps(data)
print(json_string)


data = {"name": "Alice", "age": 25}
with open("data.json", "w") as file:
    json.dump(data, file)


numbers = [1, 2, 3, 4]
with open("numbers.json", "w") as file:
    json.dump(numbers, file)


with open("data.json", "r") as file:
    data = json.load(file)
print(data)


with open("numbers.json", "r") as file:
    numbers = json.load(file)
print(numbers)