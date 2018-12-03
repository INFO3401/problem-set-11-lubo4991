
#Lucas Bouchard

#Collaberators(Steven, Harold, Justin, Zach)


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
    

rawData, df = generateDataset('simpsons_paradox.csv')


#MONDAY (11/12)

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


#2.      Compute new dependent variables that shows the percentage of students admitted and rejected for each row in the CSV. Use those rows to try to understand what significant correlations exist in this data. What factors appear to contribute most heavily to admissions? Do you think the admissions process is biased based on the available data? Why or why not?

#Compute new dep variables that show % of admitted and rejected

#df_cleaned= pd.read_csv('simpsons_paradox.csv')
#df_cleaned['Total Applicants'] = #df_cleaned['Admitted']+df_cleaned['Rejected']
#df_cleaned['Acceptance Rate'] = #df_cleaned['Admitted']/df_cleaned['Total Applicants']
#df_cleaned.to_csv('Simpsons_Paradox_Cleaned.csv')

def edit(df):
    df['Total_Applicants'] = df['Admitted'] + df['Rejected']
    df['Acceptance_Rate'] = df['Admitted']/df['Total_Applicants']
    df['Rejection_Rate'] = df['Rejected']/df['Total_Applicants']
    return df

rawData, df = generateDataset('simpsons_paradox.csv')
new_df = edit(df)

#Original Tests
print("Does gender correlate with admissions?")
men = df[(df['Gender'] == 'Male')]
women = df[(df['Gender'] == 'Female')]
runTTest(men, women, 'Admitted')
#Original P-value = 0.001774(Reject Null) "Gender does effect admissions"

print("Does department correlate with admissions?")
simpleFormula = 'Admitted ~ C(Department)'
runAnova(rawData, simpleFormula)
#P-value = .622205 (Accept Null) "Department does not effect Admissions"

print("Does gender and department correlate with admissions?")
moreComplex = 'Admitted ~ C(Department) + C(Gender)'
runAnova(rawData, moreComplex)
#P-value = Depart(.036670) / Gender (.000851) (Reject Null) "Both Gender and Department affect Admission"

#New Test
print("Does gender correlate with admissions? Is admissions bias?")
men = new_df[(new_df['Gender']=='Male')]
women = new_df[(new_df['Gender']=='Female')]
runTTest(men, women, 'Total_Applicants')
#New P-value = 0.059147(Accept Null) "Gender does not effect admissions"

#Cant Figure out why Total Applicants isn't defined here
#print("Does department correlate with admissions?")
#simpleFormula = 'Total_Applicants ~ C(Department)'
#runAnova(rawData, simpleFormula)

#print("Does gender and department correlate with admissions?")
#moreComplex = 'Total_Applicants ~ C(Department) + C(Gender)'
#runAnova(rawData, moreComplex)

####(Answer 2) 

#Based on the above test results, we can see that in the original test that "gender" did in fact influence admissions. However, once the data was corrected, we can now see evidence that neither gender or department has direct influence into admission rates. Thus admissions are not actually biased. 


#Monday (11.26)

#3. There's a data quality issue hiding in the admissions dataset from Monday. Correct this issue and compare your new results. How are they the same? How do they differ?

#   The data issue in the original CSV was that the tests were observing admissions and rejections seperatably rather than together. To fix this issue we computed the total percent of admissions based on the total amount of applicants divided by those admitted. This is why the original test was indicating bias.



















