
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


nyc_parking_violations_df=pd.read_csv(r'D:/AZUBI AFRICA FILES UPDATE/Weekly Contents/Week 9/violations.csv')
                                
nyc_parking_violations_df.head()




#dropping all NaN values in data
nyc_parking_violations_df.dropna(axis='columns', how='any', inplace=True)




nyc_parking_violations_df




#removing 99 from registration state data
nyc_parking_violations_df=nyc_parking_violations_df[nyc_parking_violations_df['Registration State']!='99']




#grouping by registration state and counting the number of tickets issued
nyc_parking_violations_per_registrationstate=nyc_parking_violations_df.groupby(by='Registration State', as_index=False).count()
nyc_parking_violations_per_registrationstate.head()





#selecting only the registration state and summons number from the nyc_parking_violations_per_registrationstate data
nyc_parking_violations_per_registrationstate[['Registration State', 'Summons Number']]
nyc_parking_violations_per_registrationstate.head()





#plotting a graph to show each registration state and the number of summons received

plt.figure(figsize=(13,6))

x=nyc_parking_violations_per_registrationstate['Summons Number']

y=nyc_parking_violations_per_registrationstate['Registration State']

plt.plot(y,x, color = 'b')

plt.xticks( rotation=90)

plt.xlabel('Registration State', fontsize=10)

plt.ylabel('Summons Number',  fontsize=10)



plt.title('Registration State and Number of Summons')

plt.tight_layout()

plt.grid(True)

plt.show





#Analysing monthly tickets issued to NY state and other states

# First we change the issue date data type to date
nyc_parking_violations_df['date'] = pd.to_datetime(nyc_parking_violations_df['Issue Date']) # Convert date to datetime
nyc_parking_violations_df['month'] = nyc_parking_violations_df['date'].dt.month #extract month from Issue Date
nyc_parking_violations_df.head()





#Number of summons by months in NY state

NYstate_tickets=nyc_parking_violations_df[nyc_parking_violations_df['Registration State']=='NY'] # NY data for all months

month_grp_NYstate=NYstate_tickets.groupby(by=NYstate_tickets['month'],as_index=False).count() #group NY data for each month
month_grp_NYstate.head()
month_grp_NYstate_sel=month_grp_NYstate[['month','Summons Number']]
month_grp_NYstate_sel





#plotting a graph to show each month and the number of summons received in NY state

plt.figure(figsize=(13,6))

x=month_grp_NYstate_sel['month']

y=month_grp_NYstate_sel['Summons Number']

plt.bar(x,y, color = 'b', width=0.5)

plt.xlabel('month', fontsize=10)

plt.ylabel('Summons Number',  fontsize=10)



plt.title('Number of Summons by Month in NY State')

plt.tight_layout()

plt.grid(True)

plt.show





#Number of summons  by month in other states

otherstates_tickets=nyc_parking_violations_df[nyc_parking_violations_df['Registration State']!='NY'] # other cities data for all months

month_grp_otherstates=otherstates_tickets.groupby(by=otherstates_tickets['month'],as_index=False).count()#group other cities data for all the months
month_grp_otherstates.head()
month_grp_otherstates_sel=month_grp_otherstates[['month','Summons Number']]
month_grp_otherstates_sel





#plotting a graph to show each month and the number of summons received in other states

plt.figure(figsize=(13,6))

x=month_grp_otherstates_sel['month']

y=month_grp_otherstates_sel['Summons Number']

plt.bar(x,y, color = 'g', width=0.5)

plt.xlabel('month', fontsize=10)

plt.ylabel('Summons Number',  fontsize=10)



plt.title('Number of Summons by Month in Other States')

plt.tight_layout()

plt.grid(True)

plt.show




#top 5 violation code from other states and number of counts 
nyc_parking_violations_df[nyc_parking_violations_df['Registration State'] != 'NY'].groupby('Violation Code')['Summons Number'].count().nlargest(5).reset_index(name='Count')


# # Report from analysis
# 
# ### 1. All NaN values were dropped from the data
# ### 2. The data type for the Issue date was changed
# ### 3. The invalid data '99' in the Registration date was removed
# ### 4. Using a plot, the registration state with the highest number of summons was shown. It showed that NY state had the highest number of summons, followed by NJ then PR.
# ### 5. Moreover, a bar chart helped us to know the month that received the highest number of summons in NY state. The highest month was the ninth month. 
# ### 6. Also, with the other states, the bar chart helped to know the month that received the highest summons. It showed that the tenth month received highest summons. 
# ### 7. Lastly we saw that the code which was most violated was the violation code 36.
# 
# ### From these analysis, I think the state can probe further to know why NY state received most summons.
# ### Also, with the months that depicted highest summons, a further research could be done to know the activities which goes on during that month that made people violate the packing rules.
# ### Lastly, knowing that the violation code 36 is the most violated, I think further research could be done to know why and probably educate the people or give some measures to prevent people from violating the code. 












