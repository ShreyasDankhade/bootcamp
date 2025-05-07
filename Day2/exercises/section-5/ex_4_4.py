import csv

def write_csv(filename, fieldnames, data):
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

fieldnames = ['name', 'age', 'location']
data = [{'name': 'Shreyas', 'age': 30, 'location': 'Wonderland'}, {'name': 'Neel', 'age': 25, 'location': 'Mumbai'}]
write_csv('output.csv', fieldnames, data)
