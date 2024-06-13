import csv


file_path = "data.csv"


with open(file_path, newline='') as file:
    reader = csv.reader(file)
    print("Data from CSV file:")
    for row in reader:
        print(row)
