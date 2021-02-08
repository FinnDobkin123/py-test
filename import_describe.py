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
        if ['smoke'] == 'yes':
            smoker.append(float(row['age']))
        elif ['smoke'] == 'no':
            non_smoker.append(float(row['age']))

#Calculate Five Number Summary for Smoker Status Age
##Import libraries
from numpy import percentile
from numpy.random import rand
##Calculate Values 
quartiles_smoker = percentile(smoker, [25, 50, 75])
quartiles_non_smoker = percentile(non_smoker[25, 50, 75])
data_min_smoker, data_max_smoker = data.min(smoker), data.max(smoker)
data_min_nonsmoker, data_max_nonsmoker = data.min(non_smoker), data.max(non_smoker)
##Print minimum and maximum values
print('The minimum age for non-smokers is ' + str(data_min_nonsmoker))
print('The maximum age for non-smokers is ' + str(data_max_nonsmoker))
print('The minimum age for smokers is ' + str(data_min_smoker))
print('The maximum age for smokers is ' + str(data_max_smoker))
##Print first quartile ages values
print("The 25th percentile of age for non smokers is " + str(quartiles_non_smoker[0]))
print("The 25th percentile of age for smokers is " + str(quartiles_smoker[0]))
##Print median ages values
print("The median age for non smokers is " + str(quartiles_non_smoker[1]))
print("The median age for smokers is " + str(quartiles_smoker[1]))
##Print first quartile ages values
print("The 75th percentile of age for non smokers is " + str(quartiles_non_smoker[2]))
print("The 75th percentile of age for smokers is " + str(quartiles_smoker[2]))

 #Determine smoking status by BMI
low_bmi = []
medium_bmi = []
high_bmi = []
with open('insurance.csv', 'r') as insurance_file:
    fieldnames = ['age', 'sex', 'bmi', 'children', 'smoke', 'region', 'charges']
    csv_reader = csv.DictReader(insurance_file, delimiter = ',', skipinitialspace=True, 
                               fieldnames = fieldnames)
    for weight in bmi:
        if row['bmi'] > 0 & row['bmi'] < 20:
           low_bmi.append(float(row['smoke'])
        elif row['bmi'] >= 20 & row['bmi'] <= 30:
           medium_bmi.append(float(row['smoke']))
        else row['bmi'] >= 30:
           high_bmi.append(float(row['smoke']))
#Create a dataframe and describe
insurance = pd.DataFrame(insurance_file) 
print insurance.describe(include = 'all')
