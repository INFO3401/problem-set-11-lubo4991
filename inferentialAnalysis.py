import numpy as np
import pandas as pd
import scipy

import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Extract the data. Return both the raw data and dataframe
def generateDataset(filename):
    data = pd.read_csv(filename)
    df = data[0:]
    df = df.dropna()
    return data, df

#Run a t-test

def runTTest(ivA, ivB, dv):
    ttest = scipy.stats.ttest_ind(ivA[dv], ivB[dv])
    print(ttest)
    
#Run ANOVA

def runAnova(data, formula):
    model = ols(formula, data).fit()
    aov_table= sm.stats.anova_lm(model, typ=2)
    print(aov_table)
    

#Run the analysis

rawData, df = generateDataset('simpsons_paradox.csv')

print("Does gender correlate with admissions?")
men = df[(df['Gender'] == 'Male')]
women = df[(df['Gender'] == 'Female')]
runTTest(men, women, 'Admitted')

print("Does department correlate with admissions?")
simpleFormula = 'Admitted ~ C(Department)'
runAnova(rawData, simpleFormula)

print("Does gender and department correlate with admissions?")
moreComplex = 'Admitted ~ C(Department) + C(Gender)'
runAnova(rawData, moreComplex)

#1. What statistical test would you use for the following scenarios? 

#(a) Does a student's current year (e.g., freshman, sophomore, etc.) effect their GPA?

#Independent variable = student's current year (categorical)
#Dependent variable = GPA (Continous)

#Stat test = T-test

#(b) Has the amount of snowfall in the mountains changed over time? 

#Independent= Time(continous)
#Dependent = Amount of snowfall(continous)

#Stat test =  Generalized Regression 

#(c) Over the last 10 years, have there been more hikers on average in Estes Park in the spring or summer? 

#Independent = Spring or Summer (season?) (categorical)
#Dependent = Number of hikers 

#Stat test = T-test

#(d) Does a student's home state predict their highest degree level?

#Independent = Home State (categorical)
#Dependent = Degresss level (categorical)

#Stat test = Chi-Squared test


#2. Compute new dependent variables that shows the percentage of students admitted and rejected for each row in the CSV. Use those rows to try to understand what significant correlations exist in this data. What factors appear to contribute most heavily to admissions? Do you think the admissions process is biased based on the available data? Why or why not?



#- 

#Monday (11.26)
#3. There's a data quality issue hiding in the admissions dataset from Monday. Correct this issue and compare your new results. How are they the same? How do they differ?


#df_cleaned= pd.read_csv('simpsons_paradox.csv')
#df_cleaned['Total Applicants'] = #df_cleaned['Admitted']+df_cleaned['Rejected']
#df_cleaned['Acceptance Rate'] = #df_cleaned['Admitted']/df_cleaned['Total Applicants']
#df_cleaned.to_csv('Simpsons_Paradox_Cleaned.csv')


rawdata2, df = generateDataset('Simpsons_Paradox_Cleaned.csv')

print("Does gender correlate with admissions?")
men = df[(df['Gender']=='Male')]
women = df[(df['Gender']=='Female')]
runTTest(men, women, 'Admitted')

print('Does department correlate with admissions?')
simpleFormula = 'Admitted ~ C(Department)'
runAnova(rawData,simpleFormula)

print("Do gender and department correlate with admissions?")
moreComplex = 'Admitted ~ C(Department) + C(Gender)'
runAnova(rawData,moreComplex)


#-The data issue in the original CSV was that the tests were only taking into account subsets of admitted and rejected applicants


















