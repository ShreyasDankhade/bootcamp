import pickle

def pickle_object(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)

def unpickle_object(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

obj = {"name": "Shreyas", "age": 30}
pickle_object(obj, "data.pkl")

loaded_obj = unpickle_object("data.pkl")
print(loaded_obj)
