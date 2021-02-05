#Import libraries
import csv
import statistics

#Read insurance.csv
import csv
with open('insurance.csv', 'r') as insurance_file:
    fieldnames = ['age', 'sex', 'bmi', 'children', 'smoke', 'region', 'charges']
    csv_reader = csv.DictReader(insurance_file, delimiter = ',', skipinitialspace=True, 
                               fieldnames = fieldnames)
    #for row in csv_reader:
        #print(row)
