import csv

def read_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row

for row in read_csv('data.csv'):
    print(row)

 