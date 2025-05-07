import json

def pretty_print_json(data):
    return json.dumps(data, indent=4, sort_keys=True)


data = {"name": "Shreyas", "age": 30, "location": "Wonderland"}
pretty_json = pretty_print_json(data)
print(pretty_json)
