class MyObject:
    def __getattr__(self, name):
        return f"Attribute '{name}' not found"

def access_custom_object_attr():
    obj = MyObject()
    return obj.some_attribute  # Will call __getattr__ since the attribute doesn't exist

result = access_custom_object_attr()
print(result)  # Output: Attribute 'some_attribute' not found
