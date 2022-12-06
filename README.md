# Exploratory-Data-Analysis
Week 9 Project

```python
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


nyc_parking_violations_df=pd.read_csv(r'D:/AZUBI AFRICA FILES UPDATE/Weekly Contents/Week 9/violations.csv')
                                
nyc_parking_violations_df.head()
```


```python
#dropping all NaN values in data
nyc_parking_violations_df.dropna(axis='columns', how='any', inplace=True)
```


```python
nyc_parking_violations_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Summons Number</th>
      <th>Plate ID</th>
      <th>Registration State</th>
      <th>Plate Type</th>
      <th>Issue Date</th>
      <th>Violation Code</th>
      <th>Issuing Agency</th>
      <th>Street Code1</th>
      <th>Street Code2</th>
      <th>Street Code3</th>
      <th>Vehicle Expiration Date</th>
      <th>Violation Precinct</th>
      <th>Issuer Precinct</th>
      <th>Issuer Code</th>
      <th>Date First Observed</th>
      <th>Law Section</th>
      <th>Vehicle Year</th>
      <th>Feet From Curb</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4714702166</td>
      <td>KGK6659</td>
      <td>NY</td>
      <td>PAS</td>
      <td>11/12/2020</td>
      <td>36</td>
      <td>V</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1180</td>
      <td>2007</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8793684599</td>
      <td>L5232HY</td>
      <td>TN</td>
      <td>PAS</td>
      <td>9/14/2020</td>
      <td>21</td>
      <td>T</td>
      <td>60790</td>
      <td>31140</td>
      <td>31190</td>
      <td>20200888</td>
      <td>101</td>
      <td>101</td>
      <td>367421</td>
      <td>0</td>
      <td>408</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8864757053</td>
      <td>BPMN76</td>
      <td>FL</td>
      <td>PAS</td>
      <td>11/25/2020</td>
      <td>20</td>
      <td>T</td>
      <td>36030</td>
      <td>31190</td>
      <td>10610</td>
      <td>20200688</td>
      <td>28</td>
      <td>28</td>
      <td>367911</td>
      <td>0</td>
      <td>408</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8778326047</td>
      <td>57387MJ</td>
      <td>NY</td>
      <td>COM</td>
      <td>8/20/2020</td>
      <td>38</td>
      <td>T</td>
      <td>34430</td>
      <td>10410</td>
      <td>13610</td>
      <td>20211231</td>
      <td>13</td>
      <td>13</td>
      <td>368567</td>
      <td>0</td>
      <td>408</td>
      <td>2016</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4706640702</td>
      <td>M81KFJ</td>
      <td>NJ</td>
      <td>PAS</td>
      <td>9/9/2020</td>
      <td>36</td>
      <td>V</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1180</td>
      <td>2002</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>49995</th>
      <td>4014245755</td>
      <td>JPN4910</td>
      <td>NY</td>
      <td>PAS</td>
      <td>6/25/2020</td>
      <td>5</td>
      <td>V</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1111</td>
      <td>2019</td>
      <td>0</td>
    </tr>
    <tr>
      <th>49996</th>
      <td>8794437506</td>
      <td>174ZYG</td>
      <td>CT</td>
      <td>PAS</td>
      <td>8/25/2020</td>
      <td>31</td>
      <td>T</td>
      <td>34030</td>
      <td>10410</td>
      <td>10510</td>
      <td>88880088</td>
      <td>6</td>
      <td>6</td>
      <td>363026</td>
      <td>0</td>
      <td>408</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>49997</th>
      <td>8849769581</td>
      <td>HES6895</td>
      <td>NY</td>
      <td>PAS</td>
      <td>11/3/2020</td>
      <td>46</td>
      <td>T</td>
      <td>27120</td>
      <td>59520</td>
      <td>49120</td>
      <td>20220413</td>
      <td>48</td>
      <td>48</td>
      <td>367900</td>
      <td>0</td>
      <td>408</td>
      <td>2005</td>
      <td>0</td>
    </tr>
    <tr>
      <th>49998</th>
      <td>8755448173</td>
      <td>63035MN</td>
      <td>NY</td>
      <td>COM</td>
      <td>8/19/2020</td>
      <td>40</td>
      <td>T</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>20211130</td>
      <td>52</td>
      <td>52</td>
      <td>364833</td>
      <td>0</td>
      <td>408</td>
      <td>2020</td>
      <td>5</td>
    </tr>
    <tr>
      <th>49999</th>
      <td>8581527528</td>
      <td>AW74165</td>
      <td>CT</td>
      <td>PAS</td>
      <td>8/6/2020</td>
      <td>20</td>
      <td>T</td>
      <td>17860</td>
      <td>25860</td>
      <td>25890</td>
      <td>20200088</td>
      <td>40</td>
      <td>40</td>
      <td>338793</td>
      <td>0</td>
      <td>408</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>50000 rows × 18 columns</p>
</div>




```python
#removing 99 from registration state data
nyc_parking_violations_df=nyc_parking_violations_df[nyc_parking_violations_df['Registration State']!='99']
```


```python
#grouping by registration state and counting the number of tickets issued
nyc_parking_violations_per_registrationstate=nyc_parking_violations_df.groupby(by='Registration State', as_index=False).count()
nyc_parking_violations_per_registrationstate.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Registration State</th>
      <th>Summons Number</th>
      <th>Plate ID</th>
      <th>Plate Type</th>
      <th>Issue Date</th>
      <th>Violation Code</th>
      <th>Issuing Agency</th>
      <th>Street Code1</th>
      <th>Street Code2</th>
      <th>Street Code3</th>
      <th>Vehicle Expiration Date</th>
      <th>Violation Precinct</th>
      <th>Issuer Precinct</th>
      <th>Issuer Code</th>
      <th>Date First Observed</th>
      <th>Law Section</th>
      <th>Vehicle Year</th>
      <th>Feet From Curb</th>
      <th>date</th>
      <th>month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AB</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AK</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AL</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AR</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
    </tr>
    <tr>
      <th>4</th>
      <td>AZ</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
    </tr>
  </tbody>
</table>
</div>




```python
#selecting only the registration state and summons number from the nyc_parking_violations_per_registrationstate data
nyc_parking_violations_per_registrationstate[['Registration State', 'Summons Number']]
nyc_parking_violations_per_registrationstate.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Registration State</th>
      <th>Summons Number</th>
      <th>Plate ID</th>
      <th>Plate Type</th>
      <th>Issue Date</th>
      <th>Violation Code</th>
      <th>Issuing Agency</th>
      <th>Street Code1</th>
      <th>Street Code2</th>
      <th>Street Code3</th>
      <th>Vehicle Expiration Date</th>
      <th>Violation Precinct</th>
      <th>Issuer Precinct</th>
      <th>Issuer Code</th>
      <th>Date First Observed</th>
      <th>Law Section</th>
      <th>Vehicle Year</th>
      <th>Feet From Curb</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AB</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AK</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AL</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
      <td>63</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AR</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
    </tr>
    <tr>
      <th>4</th>
      <td>AZ</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
    </tr>
  </tbody>
</table>
</div>




```python
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

```




    <function matplotlib.pyplot.show(close=None, block=None)>




    
![png](output_6_1.png)
    



```python
#Analysing monthly tickets issued to NY state and other states

# First we change the issue date data type to date
nyc_parking_violations_df['date'] = pd.to_datetime(nyc_parking_violations_df['Issue Date']) # Convert date to datetime
nyc_parking_violations_df['month'] = nyc_parking_violations_df['date'].dt.month #extract month from Issue Date
nyc_parking_violations_df.head()
```

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
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Summons Number</th>
      <th>Plate ID</th>
      <th>Registration State</th>
      <th>Plate Type</th>
      <th>Issue Date</th>
      <th>Violation Code</th>
      <th>Issuing Agency</th>
      <th>Street Code1</th>
      <th>Street Code2</th>
      <th>Street Code3</th>
      <th>Vehicle Expiration Date</th>
      <th>Violation Precinct</th>
      <th>Issuer Precinct</th>
      <th>Issuer Code</th>
      <th>Date First Observed</th>
      <th>Law Section</th>
      <th>Vehicle Year</th>
      <th>Feet From Curb</th>
      <th>date</th>
      <th>month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4714702166</td>
      <td>KGK6659</td>
      <td>NY</td>
      <td>PAS</td>
      <td>11/12/2020</td>
      <td>36</td>
      <td>V</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1180</td>
      <td>2007</td>
      <td>0</td>
      <td>2020-11-12</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8793684599</td>
      <td>L5232HY</td>
      <td>TN</td>
      <td>PAS</td>
      <td>9/14/2020</td>
      <td>21</td>
      <td>T</td>
      <td>60790</td>
      <td>31140</td>
      <td>31190</td>
      <td>20200888</td>
      <td>101</td>
      <td>101</td>
      <td>367421</td>
      <td>0</td>
      <td>408</td>
      <td>0</td>
      <td>0</td>
      <td>2020-09-14</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8864757053</td>
      <td>BPMN76</td>
      <td>FL</td>
      <td>PAS</td>
      <td>11/25/2020</td>
      <td>20</td>
      <td>T</td>
      <td>36030</td>
      <td>31190</td>
      <td>10610</td>
      <td>20200688</td>
      <td>28</td>
      <td>28</td>
      <td>367911</td>
      <td>0</td>
      <td>408</td>
      <td>0</td>
      <td>0</td>
      <td>2020-11-25</td>
      <td>11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8778326047</td>
      <td>57387MJ</td>
      <td>NY</td>
      <td>COM</td>
      <td>8/20/2020</td>
      <td>38</td>
      <td>T</td>
      <td>34430</td>
      <td>10410</td>
      <td>13610</td>
      <td>20211231</td>
      <td>13</td>
      <td>13</td>
      <td>368567</td>
      <td>0</td>
      <td>408</td>
      <td>2016</td>
      <td>0</td>
      <td>2020-08-20</td>
      <td>8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4706640702</td>
      <td>M81KFJ</td>
      <td>NJ</td>
      <td>PAS</td>
      <td>9/9/2020</td>
      <td>36</td>
      <td>V</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1180</td>
      <td>2002</td>
      <td>0</td>
      <td>2020-09-09</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Number of summons by months in NY state

NYstate_tickets=nyc_parking_violations_df[nyc_parking_violations_df['Registration State']=='NY'] # NY data for all months

month_grp_NYstate=NYstate_tickets.groupby(by=NYstate_tickets['month'],as_index=False).count() #group NY data for each month
month_grp_NYstate.head()
month_grp_NYstate_sel=month_grp_NYstate[['month','Summons Number']]
month_grp_NYstate_sel
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>Summons Number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>68</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>1406</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>5918</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8</td>
      <td>7818</td>
    </tr>
    <tr>
      <th>5</th>
      <td>9</td>
      <td>8178</td>
    </tr>
    <tr>
      <th>6</th>
      <td>10</td>
      <td>7748</td>
    </tr>
    <tr>
      <th>7</th>
      <td>11</td>
      <td>5622</td>
    </tr>
    <tr>
      <th>8</th>
      <td>12</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
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

```




    <function matplotlib.pyplot.show(close=None, block=None)>




    
![png](output_9_1.png)
    



```python
#Number of summons  by month in other states

otherstates_tickets=nyc_parking_violations_df[nyc_parking_violations_df['Registration State']!='NY'] # other cities data for all months

month_grp_otherstates=otherstates_tickets.groupby(by=otherstates_tickets['month'],as_index=False).count()#group other cities data for all the months
month_grp_otherstates.head()
month_grp_otherstates_sel=month_grp_otherstates[['month','Summons Number']]
month_grp_otherstates_sel
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>Summons Number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>429</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>1975</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>2827</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9</td>
      <td>2826</td>
    </tr>
    <tr>
      <th>5</th>
      <td>10</td>
      <td>3032</td>
    </tr>
    <tr>
      <th>6</th>
      <td>11</td>
      <td>2047</td>
    </tr>
  </tbody>
</table>
</div>




```python
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


```




    <function matplotlib.pyplot.show(close=None, block=None)>




    
![png](output_11_1.png)
    



```python
#top 5 violation code from other states and number of counts 
nyc_parking_violations_df[nyc_parking_violations_df['Registration State'] != 'NY'].groupby('Violation Code')['Summons Number'].count().nlargest(5).reset_index(name='Count')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Violation Code</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>36</td>
      <td>2798</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>1794</td>
    </tr>
    <tr>
      <th>2</th>
      <td>14</td>
      <td>1160</td>
    </tr>
    <tr>
      <th>3</th>
      <td>38</td>
      <td>1089</td>
    </tr>
    <tr>
      <th>4</th>
      <td>40</td>
      <td>1075</td>
    </tr>
  </tbody>
</table>
</div>



# Report from analysis

### 1. All NaN values were dropped from the data
### 2. The data type for the Issue date was changed
### 3. The invalid data '99' in the Registration date was removed
### 4. Using a plot, the registration state with the highest number of summons was shown. It showed that NY state had the highest number of summons, followed by NJ then PR.
### 5. Moreover, a bar chart helped us to know the month that received the highest number of summons in NY state. The highest month was the ninth month. 
### 6. Also, with the other states, the bar chart helped to know the month that received the highest summons. It showed that the tenth month received highest summons. 
### 7. Lastly we saw that the code which was most violated was the violation code 36.

### From these analysis, I think the state can probe further to know why NY state received most summons.
### Also, with the months that depicted highest summons, a further research could be done to know the activities which goes on during that month that made people violate the packing rules.
### Lastly, knowing that the violation code 36 is the most violated, I think further research could be done to know why and probably educate the people or give some measures to prevent people from violating the code. 


```python

```


```python

```
