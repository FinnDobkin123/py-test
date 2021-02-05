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

#Determine smoker ages
smoker = []
non_smoker = []
with open('insurance.csv', 'r') as insurance_file:
    fieldnames = ['age', 'sex', 'bmi', 'children', 'smoke', 'region', 'charges']
    csv_reader = csv.DictReader(insurance_file, delimiter = ',', skipinitialspace=True, 
                               fieldnames = fieldnames)
    for status in insurance_file:
        if row['smoke'] == 'yes':
            smoker.append(float(row['age']))
        elif row['smoke'] == 'no':
            non_smoker.append(float(row['age']))
