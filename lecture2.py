import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "sakila.db")


conn = sqlite3.connect(db_path)



df = pd.read_sql('''
    SELECT
        rental.rental_id, rental.rental_date, rental.return_date,
        customer.last_name AS customer_lastname,
        store.store_id,
        city.city AS rental_store_city,
        film.title AS film_title, film.rental_duration AS film_rental_duration,
        film.rental_rate AS film_rental_rate, film.replacement_cost AS film_replacement_cost,
        film.rating AS film_rating
    FROM rental
    INNER JOIN customer ON rental.customer_id == customer.customer_id
    INNER JOIN inventory ON rental.inventory_id == inventory.inventory_id
    INNER JOIN store ON inventory.store_id == store.store_id
    INNER JOIN address ON store.address_id == address.address_id
    INNER JOIN city ON address.city_id == city.city_id
    INNER JOIN film ON inventory.film_id == film.film_id
    ;
''', conn, index_col='rental_id', parse_dates=['rental_date', 'return_date'])

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df['film_rental_rate'].describe())
df['film_rental_rate'].plot(kind='box',vert=False,figsize=(14,6))
plt.show()

ax = df['film_rental_rate'].value_counts().plot(kind='bar', figsize=(14,6))
ax.set_ylabel('Number of Rentals')
plt.show()

df['rental_gain_return'] = (df['film_rental_rate'] / df['film_replacement_cost'])* 100
print(df['rental_gain_return'].head())

df['rental_gain_return'].plot(kind='density', figsize=(14,6))
plt.show()

ax=df['rental_gain_return'].plot(kind='density',figsize=(14,6))
ax.axvline(df['rental_gain_return'].mean(),color='red')
ax.axvline(df['rental_gain_return'].median(),color='green')
plt.show()

print(df.loc[df['customer_lastname'] == 'HANSEN'])

print(df['film_replacement_cost'].max())
print(df.loc[df['film_replacement_cost']==df['film_replacement_cost'].max(),'film_title'].unique())

print(df.loc[(df['film_rating']=='PG') | (df['film_rating']=='PG-13')].shape[0])