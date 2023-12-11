# Project goals

- Find the key drivers of Loan Default.

# Project description

- I've been tasked to find the key drivers of Loan Defaulting. With the Data I have been given.

# My Plan
### Initial hypotheses: 

- To see if Debt to income and Credit Score are key contributors to Loan Default.

## Acquire:
- imported data via csv from kaggle. The csv came from coursera. An online Data Science learning website.

- CSV contained 255,347 Rows & 18 Columns

- each row represented a single individual and whether their loan defaulted or not. Along with information about the individual.

- each column represents specific information, how much income, married, credit score, intrest rate, etc.

## Prepare:
### Prepare Actions
 
 ### Renamed_columns: 
 
'LoanID','Age','Income','LoanAmount','CreditScore','MonthsEmployed','NumCreditLines', 'InterestRate','LoanTerm','DTIRatio','Education'	'EmploymentType','MaritalStatus','HasMortgage'	'HasDependents','LoanPurpose','HasCoSigner','Default'

### checked data for indescripencies:
 
- data had no nulls or missing values
- no outliers 
- encoded all yes and no values to 1's & 0's
- split data into train, validate, test


## Modeling:
Using XGBoost feature importance I was able to gather information about the drivers and find out specifically which drivers caused Loan Default. With that information I proceeded to feed that data into an XGBoost Classifier. 
## Data dictionary:

## Features and Definitions: 
 
 | Feature           | Definition                                            |
|-------------------|-------------------------------------------------------|
| age               | Age of the individual                                  |
| income            | Income of the individual                               |
| loan_amount       | Amount of the loan                           |
| credit_score      | Credit score of the individual                         |
| months_employed   | Number of months employed                              |
| no_credit_lines   | Number of credit lines                                 |
| interest_rate     | Interest rate on the loan                              |
| loan_term         | Term (duration) of the loan                            |
| debt_income_ratio | Debt-to-Income ratio                                   |
| education         | Educational level of the individual                    |
| employment_type   | Type of employment                                     |
| marital_status    | Marital status of the individual                       |
| mortgage          | Presence of a mortgage (Yes/No)                        |
| dependents        | Presence of dependents (Yes/No)                        |
| loan_purpose      | Purpose of the loan                                    |
| cosigner          | Presence of a co-signer (Yes/No)                       


### Key findings:

- Some of my key findings is that the Loan Amount, Income, Intrest Rate and Age were the main drivers for loan default. 

- Model of XGBoost Classifier worked best with the data by beating baseline by 1 percent. 

## Takeaways and Conclusions:

- Though my model beat baseline by 1 percent. That is significant given that the data set I used had a 88 percent loans not defaulting. 


- I think with more time and more data specifically geared toward loan default we can come up with more percise information as to why loans defualt. 
## Recommendations:

- For my recommendations I would like to take more time to evaluate the data and get a more current data set. With the economy in the state that it is now. I am curious to see if there have been more loan Defaults. 

- Upon further investigation I will be able to come up with more viable solutions to help prevent Loan Default.