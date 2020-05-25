# --------------
import pandas as pd
import numpy as np
from scipy.stats import mode 

bank=pd.read_csv(path)

categorical_var=bank.select_dtypes(include = 'object')

numerical_var=bank.select_dtypes(include = 'number')

bank.drop('Loan_ID',axis=1,inplace=True)

banks=bank

bank_mode=banks.mode().iloc[0]

banks.fillna(bank_mode,inplace=True)

avg_loan_amount=bank.pivot_table(index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')

loan_approved_se = len(banks[(banks.Self_Employed=='Yes') & (banks.Loan_Status=='Y')])

loan_approved_nse = len(banks[(banks.Self_Employed=='No') & (banks.Loan_Status=='Y')])

percentage_se = float(loan_approved_se*100)/len(banks['Self_Employed'])

percentage_nse = float(loan_approved_nse*100)/len(banks['Self_Employed'])

loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12 )

big_loan_term=len(loan_term[loan_term>=25])

loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby['ApplicantIncome','Credit_History']

mean_values = loan_groupby.mean()


