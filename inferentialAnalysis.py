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

#-----

#Independent variable = student's current year (categorical)
#Dependent variable = GPA (Continous)

#Simple Regression






#(b) Has the amount of snowfall in the mountains changed over time? 

#Independent= Time(continous)
#Dependent = Amount of snowfall(continous)

#Pearson correlation  

#(c) Over the last 10 years, have there been more hikers on average in Estes Park in the spring or summer? 

#Independent = Spring or Summer (season?) (categorical)
#Dependent = Number of hikers 


#(d) Does a student's home state predict their highest degree level?

#2. You've been given some starter code in class that shows you how to set up ANOVAs and Student's T-Tests in addition to the regression code from the last few weeks. Now, use this code to more deeply explore the simpsons_paradox.csv dataset. Compute new dependent variables that shows the percentage of students admitted and rejected for each row in the CSV. Use those rows to try to understand what significant correlations exist in this data. What factors appear to contribute most heavily to admissions? Do you think the admissions process is biased based on the available data? Why or why not?