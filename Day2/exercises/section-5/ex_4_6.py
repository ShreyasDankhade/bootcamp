import json

def secure_unpickling(data):
    # Deserialize JSON safely
    return json.loads(data)

safe_json_data = '{"name": "Shreyas", "age": 30}'
safe_data = secure_unpickling(safe_json_data)
print(safe_data)
