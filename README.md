# Exploratory-Data-Analysis
Week 9 Project

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
​
​
nyc_parking_violations_df=pd.read_csv(r'D:/AZUBI AFRICA FILES UPDATE/Weekly Contents/Week 9/violations.csv')
                                
nyc_parking_violations_df.head()

## dropping all NaN values in data
nyc_parking_violations_df.dropna(axis='columns', how='any', inplace=True)
nyc_parking_violations_df
Summons Number	Plate ID	Registration State	Plate Type	Issue Date	Violation Code	Issuing Agency	Street Code1	Street Code2	Street Code3	Vehicle Expiration Date	Violation Precinct	Issuer Precinct	Issuer Code	Date First Observed	Law Section	Vehicle Year	Feet From Curb
0	4714702166	KGK6659	NY	PAS	11/12/2020	36	V	0	0	0	0	0	0	0	0	1180	2007	0
1	8793684599	L5232HY	TN	PAS	9/14/2020	21	T	60790	31140	31190	20200888	101	101	367421	0	408	0	0
2	8864757053	BPMN76	FL	PAS	11/25/2020	20	T	36030	31190	10610	20200688	28	28	367911	0	408	0	0
3	8778326047	57387MJ	NY	COM	8/20/2020	38	T	34430	10410	13610	20211231	13	13	368567	0	408	2016	0
4	4706640702	M81KFJ	NJ	PAS	9/9/2020	36	V	0	0	0	0	0	0	0	0	1180	2002	0
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
49995	4014245755	JPN4910	NY	PAS	6/25/2020	5	V	0	0	0	0	0	0	0	0	1111	2019	0
49996	8794437506	174ZYG	CT	PAS	8/25/2020	31	T	34030	10410	10510	88880088	6	6	363026	0	408	0	0
49997	8849769581	HES6895	NY	PAS	11/3/2020	46	T	27120	59520	49120	20220413	48	48	367900	0	408	2005	0
49998	8755448173	63035MN	NY	COM	8/19/2020	40	T	0	0	0	20211130	52	52	364833	0	408	2020	5
49999	8581527528	AW74165	CT	PAS	8/6/2020	20	T	17860	25860	25890	20200088	40	40	338793	0	408	0	0
50000 rows × 18 columns

## removing 99 from registration state data
nyc_parking_violations_df=nyc_parking_violations_df[nyc_parking_violations_df['Registration State']!='99']
#grouping by registration state and counting the number of tickets issued
nyc_parking_violations_per_registrationstate=nyc_parking_violations_df.groupby(by='Registration State', as_index=False).count()
nyc_parking_violations_per_registrationstate.head()
Registration State	Summons Number	Plate ID	Plate Type	Issue Date	Violation Code	Issuing Agency	Street Code1	Street Code2	Street Code3	Vehicle Expiration Date	Violation Precinct	Issuer Precinct	Issuer Code	Date First Observed	Law Section	Vehicle Year	Feet From Curb	date	month
0	AB	4	4	4	4	4	4	4	4	4	4	4	4	4	4	4	4	4	4	4
1	AK	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3
2	AL	63	63	63	63	63	63	63	63	63	63	63	63	63	63	63	63	63	63	63
3	AR	13	13	13	13	13	13	13	13	13	13	13	13	13	13	13	13	13	13	13
4	AZ	143	143	143	143	143	143	143	143	143	143	143	143	143	143	143	143	143	143	143

## selecting only the registration state and summons number from the nyc_parking_violations_per_registrationstate data
nyc_parking_violations_per_registrationstate[['Registration State', 'Summons Number']]
nyc_parking_violations_per_registrationstate.head()
Registration State	Summons Number	Plate ID	Plate Type	Issue Date	Violation Code	Issuing Agency	Street Code1	Street Code2	Street Code3	Vehicle Expiration Date	Violation Precinct	Issuer Precinct	Issuer Code	Date First Observed	Law Section	Vehicle Year	Feet From Curb
0	AB	4	4	4	4	4	4	4	4	4	4	4	4	4	4	4	4	4
1	AK	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3
2	AL	63	63	63	63	63	63	63	63	63	63	63	63	63	63	63	63	63
3	AR	13	13	13	13	13	13	13	13	13	13	13	13	13	13	13	13	13
4	AZ	143	143	143	143	143	143	143	143	143	143	143	143	143	143	143	143	143

## plotting a graph to show each registration state and the number of summons received
​
plt.figure(figsize=(13,6))
​
x=nyc_parking_violations_per_registrationstate['Summons Number']
​
y=nyc_parking_violations_per_registrationstate['Registration State']
​
plt.plot(y,x, color = 'b')
​
plt.xticks( rotation=90)
​
plt.xlabel('Registration State', fontsize=10)
​
plt.ylabel('Summons Number',  fontsize=10)
​
​
​
plt.title('Registration State and Number of Summons')
​
plt.tight_layout()
​
plt.grid(True)
​
plt.show
​
<function matplotlib.pyplot.show(close=None, block=None)>

#Analysing monthly tickets issued to NY state and other states
​
# First we change the issue date data type to date
nyc_parking_violations_df['date'] = pd.to_datetime(nyc_parking_violations_df['Issue Date']) # Convert date to datetime
nyc_parking_violations_df['month'] = nyc_parking_violations_df['date'].dt.month #extract month from Issue Date
nyc_parking_violations_df.head()
C:\Users\USER\AppData\Local\Temp\ipykernel_9348\2517604418.py:2: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  nyc_parking_violations_df['date'] = pd.to_datetime(nyc_parking_violations_df['Issue Date']) # Convert date to datetime
C:\Users\USER\AppData\Local\Temp\ipykernel_9348\2517604418.py:3: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  nyc_parking_violations_df['month'] = nyc_parking_violations_df['date'].dt.month #extract month from Issue Date
Summons Number	Plate ID	Registration State	Plate Type	Issue Date	Violation Code	Issuing Agency	Street Code1	Street Code2	Street Code3	Vehicle Expiration Date	Violation Precinct	Issuer Precinct	Issuer Code	Date First Observed	Law Section	Vehicle Year	Feet From Curb	date	month
0	4714702166	KGK6659	NY	PAS	11/12/2020	36	V	0	0	0	0	0	0	0	0	1180	2007	0	2020-11-12	11
1	8793684599	L5232HY	TN	PAS	9/14/2020	21	T	60790	31140	31190	20200888	101	101	367421	0	408	0	0	2020-09-14	9
2	8864757053	BPMN76	FL	PAS	11/25/2020	20	T	36030	31190	10610	20200688	28	28	367911	0	408	0	0	2020-11-25	11
3	8778326047	57387MJ	NY	COM	8/20/2020	38	T	34430	10410	13610	20211231	13	13	368567	0	408	2016	0	2020-08-20	8
4	4706640702	M81KFJ	NJ	PAS	9/9/2020	36	V	0	0	0	0	0	0	0	0	1180	2002	0	2020-09-09	9
#Number of summons by months in NY state
​
NYstate_tickets=nyc_parking_violations_df[nyc_parking_violations_df['Registration State']=='NY'] # NY data for all months
​
month_grp_NYstate=NYstate_tickets.groupby(by=NYstate_tickets['month'],as_index=False).count() #group NY data for each month
month_grp_NYstate.head()
month_grp_NYstate_sel=month_grp_NYstate[['month','Summons Number']]
month_grp_NYstate_sel
month	Summons Number
0	2	2
1	5	68
2	6	1406
3	7	5918
4	8	7818
5	9	8178
6	10	7748
7	11	5622
8	12	1

## plotting a graph to show each month and the number of summons received in NY state
​
plt.figure(figsize=(13,6))
​
x=month_grp_NYstate_sel['month']
​
y=month_grp_NYstate_sel['Summons Number']
​
plt.bar(x,y, color = 'b', width=0.5)
​
plt.xlabel('month', fontsize=10)
​
plt.ylabel('Summons Number',  fontsize=10)
​
​
​
plt.title('Number of Summons by Month in NY State')
​
plt.tight_layout()
​
plt.grid(True)
​
plt.show
​
<function matplotlib.pyplot.show(close=None, block=None)>

#Number of summons  by month in other states
​
otherstates_tickets=nyc_parking_violations_df[nyc_parking_violations_df['Registration State']!='NY'] # other cities data for all months
​
month_grp_otherstates=otherstates_tickets.groupby(by=otherstates_tickets['month'],as_index=False).count()#group other cities data for all the months
month_grp_otherstates.head()
month_grp_otherstates_sel=month_grp_otherstates[['month','Summons Number']]
month_grp_otherstates_sel
month	Summons Number
0	5	33
1	6	429
2	7	1975
3	8	2827
4	9	2826
5	10	3032
6	11	2047

## plotting a graph to show each month and the number of summons received in other states
​
plt.figure(figsize=(13,6))
​
x=month_grp_otherstates_sel['month']
​
y=month_grp_otherstates_sel['Summons Number']
​
plt.bar(x,y, color = 'g', width=0.5)
​
plt.xlabel('month', fontsize=10)
​
plt.ylabel('Summons Number',  fontsize=10)
​
​
​
plt.title('Number of Summons by Month in Other States')
​
plt.tight_layout()
​
plt.grid(True)
​
plt.show
​
​
<function matplotlib.pyplot.show(close=None, block=None)>

#top 5 violation code from other states and number of counts 
nyc_parking_violations_df[nyc_parking_violations_df['Registration State'] != 'NY'].groupby('Violation Code')['Summons Number'].count().nlargest(5).reset_index(name='Count')
Violation Code	Count
0	36	2798
1	21	1794
2	14	1160
3	38	1089
4	40	1075

# Report from analysis
1. All NaN values were dropped from the data
2. The data type for the Issue date was changed
3. The invalid data '99' in the Registration date was removed
4. Using a plot, the registration state with the highest number of summons was shown. It showed that NY state had the highest number of summons, followed by NJ then PR.
5. Moreover, a bar chart helped us to know the month that received the highest number of summons in NY state. The highest month was the ninth month.
6. Also, with the other states, the bar chart helped to know the month that received the highest summons. It showed that the tenth month received highest summons.
7. Lastly we saw that the code which was most violated was the violation code 36.
From these analysis, I think the state can probe further to know why NY state received most summons.
Also, with the months that depicted highest summons, a further research could be done to know the activities which goes on during that month that made people violate the packing rules.
Lastly, knowing that the violation code 36 is the most violated, I think further research could be done to know why and probably educate the people or give some measures to prevent people from violating the code.