import csv

def filter_csv_rows(file_path, condition):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if condition(row):
                yield row

def condition(row):
    return int(row['age']) > 30

for row in filter_csv_rows('data.csv', condition):
    print(row)
