#Import libraries
import csv
import statistics

#Read insurance.csv
import csv
with open('insurance.csv', 'r') as insurance_file:
    csv_reader = csv.DictReader(insurance_file, delimiter = ',', skipinitialspace=True)
    for row in csv_reader:
        print(row)
