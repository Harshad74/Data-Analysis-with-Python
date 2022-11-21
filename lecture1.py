import pandas as pd
import matplotlib.pyplot as plt

sales=pd.read_csv(r'C:\Users\JITENDRA\Desktop\Git\Data-Analysis-with-Python\sales_data.csv')
print(sales.head())
print(sales.shape)
print(sales.info())
print(sales.describe())
print(sales['Unit_Cost'].describe())
print(sales['Unit_Cost'].median())

sales['Unit_Cost'].plot(kind='box',vert=False,figsize=(14,6))
plt.show()

sales['Unit_Cost'].plot(kind='density', figsize=(14,6))
plt.show()

ax=sales['Unit_Cost'].plot(kind='hist',figsize=(14,6))
ax.set_ylabel('Number of sales')
ax.set_xlabel('dollars')
plt.show()

print(sales['Age_Group'].value_counts())
sales['Age_Group'].value_counts().plot(kind='pie', figsize=(6,6))
plt.show()

corr=sales.corr()
print(corr)

sales['Revenue_per_age']=sales['Revenue']/sales['Customer_Age']
print(sales['Revenue_per_age'].head())


sales['Calculated_Cost']=sales['Order_Quantity']*sales['Unit_Cost']
print(sales['Calculated_Cost'].head())

print((sales['Calculated_Cost'] != sales['Cost']).sum())

sales.plot(kind='scatter',x='Calculated_Cost',y='Profit',fig=(6,6))
plt.show()

print(sales.loc[sales['State']=='Kentucky'])
print(sales.loc[sales['Age_Group']=='Adults (35-64)','Revenue'].mean())

print(sales.loc[(sales['Age_Group']=='Youth (<25)') | (sales['Age_Group']=='Adults (35-64)')].shape[0])
print(sales.loc[(sales['Age_Group']=='Adults (35-64)') & (sales['Country']=='United States'),'Revenue'].mean())
sales.loc[sales['Country']=='France','Revenue']*1.1
print((sales.loc[sales['Country']=='France','Revenue']*1.1).head())

