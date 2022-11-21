import pandas as pd
import numpy as np

g7_pop=pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])
print(g7_pop)

g7_pop.name='G7 Population in millions'

print(g7_pop.values)
print(type(g7_pop.values))
print(g7_pop.index)
g7_pop.index=['Canada','France','Germany','Italy','Japan','United Kingdom','United States',]
print(g7_pop)
p=pd.Series([35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523],index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom',
       'United States'],name='G7 population in millions')
print(p)
print(pd.Series(g7_pop,index=['France', 'Germany', 'Italy', 'Spain']))
print(g7_pop.iloc[0])
print(g7_pop['Canada':'Italy'])
print(g7_pop>70)
print(g7_pop[g7_pop>70])
print(g7_pop.std())

g7_pop.iloc[-1]=500
print(g7_pop)

g7_pop[g7_pop<70]=99.99
print(g7_pop)


# Pandas Dataframes

df=pd.DataFrame({'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],'Continent': [
        'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

print(df)
df.index=['Canada','France','Germany','Italy','Japan','United Kingdom','United States']
print(df)
print(df.shape)
print(df.describe())
print(df.dtypes.value_counts())
print(df['Population'].to_frame())
print(df[['Population','GDP']])
print(df[1:3])
print(df.loc['Italy'].to_frame())
print(df.iloc[-1])
print(df.iloc[[0,1,-1]])

print(df.loc[df['Population']>70,['Population','GDP']])
print(df.drop(['Canada','Japan']))

print(df.drop(['Population','HDI'],axis=1))

crisis=pd.Series([-1_000_000,-0.3],index=['GDP','HDI'])
print(df[['GDP','HDI']]+crisis)

langs=pd.Series(['French', 'German', 'Italian'],index=['France', 'Germany', 'Italy'],name='Language')
df['Language']=langs
print(df)

print(df.rename(columns={'HDI':'Human Development Index','Anual Popcorn Consumption': 'APC'},index={'United States':'USA','United Kingdom':'UK','Argentina':'AR'}))

print(df.rename(index=lambda x: x.lower()))

df.drop(columns=['Language'],inplace=True)
print(df)

df.loc['China']=pd.Series({'Population':1_400_000_000,'Continent':'Asia'})
print(df)

print(df.reset_index())
print(df.set_index('Population'))

population=df['Population']
print(population)
print(population.quantile(.25))
print(population.quantile([.2,.4,.6,.8,1]))