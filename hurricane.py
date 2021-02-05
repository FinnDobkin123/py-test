#Import libraries and create lists
import csv
import statistics

age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

#Import dataset
with open("insurance.csv", newline = "") as insurance_data:
    dataset = csv.DictReader(insurance_data, delimiter = ",")
    headers = dataset.fieldnames 
    listed_headers = list(headers)
    dict_parameters = {}
    
    for header in headers:
        dict_parameters.update({str(header): []})
    
    for row in dataset:
        for header, value in zip(headers, dict_parameters.values()):
            value.append(row[header])
