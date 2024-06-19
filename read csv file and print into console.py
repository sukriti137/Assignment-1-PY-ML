import csv

# Specify the path to your CSV file
file_path = 'path/to/your/file.csv'

# Open the CSV file
with open(file_path, mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Read and print each row of the CSV file
    for row in csv_reader:
        print(row)
