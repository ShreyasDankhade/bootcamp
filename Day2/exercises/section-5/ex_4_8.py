import csv
from collections import namedtuple

def read_csv_as_namedtuple(filename, named_tuple_type):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [named_tuple_type(**row) for row in reader]

Person = namedtuple('Person', ['name', 'age', 'location'])
people = read_csv_as_namedtuple('data.csv', Person)
for person in people:
    print(person)