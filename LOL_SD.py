# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:36:16 2020

@author: CerroF



Wikipedia Definition
The interquartile range (IQR), also called the midspread or middle 50%, or technically H-spread, is a measure of statistical dispersion, being equal to the difference between 75th and 25th percentiles, or between upper and lower quartiles, IQR = Q3 − Q1.
In other words, the IQR is the first quartile subtracted from the third quartile; these quartiles can be clearly seen on a box plot on the data.
It is a measure of the dispersion similar to standard deviation or variance, but is much more robust against outliers.

"""

# Import required libraries

pip install xlwt

import xlwt

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy
import scipy.stats as stats
import math
import scipy.stats




df = pd.read_excel(open('./LOI S1 April 2020.xlsx', 'rb'),
              sheet_name='IDS')  


print(df['Time'].describe(),
     'Mode:', df['Time'].mode(),
     'Median:', df['Time'].median())



#x_min = df['Time'].min()
x_min = 0
x_max = df['Time'].max()

mean = df['Time'].mean()
std = df['Time'].std()

x = np.linspace(x_min, x_max, 100)

y = scipy.stats.norm.pdf(x,mean,std)

plt.plot(x,y, color='coral')

plt.grid()

plt.xlim(x_min,x_max)
plt.ylim(0,0.05)

plt.title('Original distribution',fontsize=12)

plt.xlabel('x')
plt.ylabel('Normal Distribution')

plt.savefig("normal_distribution.png")
print(plt.show())

#CLEANED DATA USING IQR

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
IQR1=print(IQR)


result=((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR)))



result.to_excel('./IDs_To_Match.xlsx', sheet_name='IDs')

df_out = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]



print(df_out['Time'].describe(),
     'Mode:', df_out['Time'].mode(),
     'Median:', df_out['Time'].median())



x_min = df_out['Time'].min()
x_max = df_out['Time'].max()

mean = df_out['Time'].mean()
std = df_out['Time'].std()

x = np.linspace(x_min, x_max, 100)

y = scipy.stats.norm.pdf(x,mean,std)

plt.plot(x,y, color='coral')

plt.grid()

plt.xlim(x_min,x_max)
plt.ylim(0,0.20)

plt.title('Cleaned distribution',fontsize=12)

plt.xlabel('x')
plt.ylabel('Normal Distribution')

plt.savefig("normal_distribution.png")
print(plt.show())




