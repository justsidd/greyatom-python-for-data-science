# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
#data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file
data = pd.read_csv(path)

#Creating a new variable to store the value counts

loan_status = data.Loan_Status.value_counts()

#Plotting bar plot
loan_status.plot(kind = 'bar')

# Step 2
#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area','Loan_Status'])
property_and_loan = property_and_loan.size().unstack()
property_and_loan.plot(kind= 'bar',stacked=False)

#Changing the x-axis label
plt.xlabel = 'Property_Area'

#Changing the y-axis label
plt.ylabel = 'Loan Status'

#Rotating the ticks of X-axis
plt.xtick = 45

# Step 3
#Plotting a stacked bar plot

education_and_loan = data.groupby(['Education','Loan_Status'])
education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot(kind='bar',stacked = True)


#Changing the x-axis label
plt.xlabel ='Education Status'
#Changing the y-axis label
plt.ylabel = 'Loan Status'

#Rotating the ticks of X-axis
plt.xtick = 45 

# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate = data[data['Education'] == 'Graduate']

#Subsetting the dataframe based on 'Education' column
not_graduate = data[data['Education'] == 'Not Graduate']

#Plotting density plot for 'Graduate'
graduate.LoanAmount.plot(kind = 'density',label = 'Graduate')

#Plotting density plot for 'Graduate'
not_graduate.LoanAmount.plot(kind = 'density',label = 'Not Graduate')

#For automatic legend display

# Step 5
#Setting up the subplots
fig,(ax_1,ax_2,ax_3) = plt.subplots(3,1)

#Plotting scatter plot
data.plot.scatter(x ='ApplicantIncome',y= 'LoanAmount',ax =ax_1,title='Applicant Income')

#Setting the subplot axis title
#Plotting scatter plot
data.plot.scatter(x ='CoapplicantIncome',y= 'LoanAmount',ax =ax_2,title='Coapplicant Income')

#Setting the subplot axis title


#Creating a new column 'TotalIncome'
data['TotalIncome']= data['ApplicantIncome'] +data['CoapplicantIncome']
data['TotalIncome'] = data.TotalIncome.apply(lambda x :int(x))
#Plotting scatter plot
data.plot.scatter(x ='TotalIncome',y= 'LoanAmount',ax =ax_3,title='Total Income')




