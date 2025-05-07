import csv

def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]


csv_data = read_csv('data.csv')
print(csv_data)
