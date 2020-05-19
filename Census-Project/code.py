# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate([data,new_record],axis=0)

age=np.asarray(census[:,0])

max_age=np.max(age)
min_age=np.min(age)

mean_age=np.mean(age)
age_std=np.std(age)

race_0=[x for x in census[:,2] if x==0.0]
race_1=[x for x in census[:,2] if x==1.0]
race_2=[x for x in census[:,2] if x==2.0]
race_3=[x for x in census[:,2] if x==3.0]
race_4=[x for x in census[:,2] if x==4.0]

race_0=np.asarray(race_0)
race_1=np.asarray(race_1)
race_2=np.asarray(race_2)
race_3=np.asarray(race_3)
race_4=np.asarray(race_4)

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

mini=[len_0,len_1,len_2,len_3,len_4]

minority_race=mini.index(min(mini))

senior_citizens=[x for x in census[:,0] if x>60]

senior_citizens=np.asarray(senior_citizens)

working_hours_sum=0

for x in range(len(census)):
	if census[x,0]>60:
		working_hours_sum+=census[x,6]

senior_citizens_len=len(senior_citizens)

avg_working_hours=(working_hours_sum/senior_citizens_len)

high=[x for x in census[:,1] if x>10]
high=np.asarray(high)

low=[x for x in census[:,1] if x<=10]
low=np.asarray(low)

avg_pay_high=[]
avg_pay_low=[]

for x in range(len(census)):
	if census[x,1]>10:
		avg_pay_high.append(census[x,7])
	elif census[x,1]<=10:
		avg_pay_low.append(census[x,7])

avg_pay_low=np.asarray(avg_pay_low)
avg_pay_high=np.asarray(avg_pay_high)

avg_pay_low=np.mean(avg_pay_low)
avg_pay_high=np.mean(avg_pay_high)

avg_pay_high==avg_pay_low



