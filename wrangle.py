import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import xgboost as xgb
from sklearn.metrics import accuracy_score

import warnings
warnings.filterwarnings('ignore')

# Create a dictionary mapping old column names to new column names
# Replace the keys with your existing column names and the values with the new names
def clean_data(df):
    """
    With this function we are changing the column names by mapping and replacing the old columns 
    with the new columns names.Setting Loan ID to index and then changing Yes and No to 1's and 0's
    
    """
    
    
    
    column_mapping = {
    'LoanID': 'loan_id',
    'Age': 'age',
    'Income': 'income',
    'LoanAmount': 'loan_amount',
    'CreditScore': 'credit_score',
    'MonthsEmployed': 'months_employed',
    'NumCreditLines': 'no_credit_lines',
    'InterestRate': 'interest_rate',
    'LoanTerm': 'loan_term',
    'DTIRatio': 'debt_income_ratio',
    'Education': 'education',
    'EmploymentType': 'employment_type',
    'MaritalStatus' :'marital_status',
    'HasMortgage' :'mortgage',
    'HasDependents' :'dependents',
    'LoanPurpose' :'loan_purpose',
    'HasCoSigner' :'cosigner',
    'Default' : 'defaulted'}
    # Rename columns using the mapping
    df.rename(columns=column_mapping, inplace=True)
     # Set 'loan_id' as the index
    df.set_index('loan_id', inplace=True)
    # just changing yes and no's to ones and zero's
    df['mortgage'] = df['mortgage'].replace({'Yes': 1, 'No': 0})
    df['dependents'] = df['dependents'].replace({'Yes': 1, 'No': 0})
    df['cosigner'] = df['cosigner'].replace({'Yes': 1, 'No': 0})
    
    return df





def cred_rating(row):
    """
    creates a new column in my df that seperates credit score based on low, average, high
    
    
    """
    
    
    if 300 <= row['credit_score'] <=  575:
        return 'low'
   
    elif 576 <= row['credit_score'] <= 700:
        return 'average'
    
    elif 701 <= row['credit_score'] <= 850:
        return 'high'



    
    
    
    
    
    
# Split data
def split_data(df):
    '''
    split continuouse data into train, validate, test;target variable being qualit

    returns train, validate, test
    '''

    train_val, test = train_test_split(df,
                                   train_size=0.8,
                                   random_state=123,
                                   stratify = df['defaulted'])
    train, validate = train_test_split(train_val,
                                   train_size=0.75,
                                   random_state=123,
                                   stratify=train_val['defaulted'])
    
    print(f'Train: {len(train)/len(df)}')
    print(f'Validate: {len(validate)/len(df)}')
    print(f'Test: {len(test)/len(df)}')
    

    return train, validate, test


def defaulted_overall(df):
    '''plots overall loan responses
    of the data frame and returns 
    a bargraph'''
    # create a figure
    fig = plt.figure(figsize=(12, 6)) 
    ax = fig.add_subplot(111)

    # proportion of observation of each class
    prop_response = df['defaulted'].value_counts(normalize=True)

    # create a bar plot showing the percentage of churn
    prop_response.plot(kind='bar', 
                    ax=ax)


    # set title and labels
    ax.set_title('Percentage not defaulted vs defaulted',
                fontsize=18)
    ax.set_xlabel('loan_status',
                fontsize=14)
    ax.set_ylabel('Percentage of data',
                fontsize=14)
    ax.tick_params(rotation='auto')













