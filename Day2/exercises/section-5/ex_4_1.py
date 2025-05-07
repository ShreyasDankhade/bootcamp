import json

def serialize_dict_to_json(data):
    return json.dumps(data)

def deserialize_json_to_dict(json_string):
    return json.loads(json_string)

data = {"name": "Shreyas", "age": 30}
json_data = serialize_dict_to_json(data)
print(json_data)  # Output: '{"name": "Shreyas", "age": 30}'

deserialized_data = deserialize_json_to_dict(json_data)
print(deserialized_data)  # Output: {'name': 'Shreyas', 'age': 30}
