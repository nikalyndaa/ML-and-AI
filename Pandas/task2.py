# У CSV-файлі містяться дані про замовлення: "Номер замовлення", "Клієнт", "Дата", "Сума".
# 이
# Прочитайте дані з файлу в Data Frame.
# Виведіть перші десять рядків.
# Визначте кількість замовлень кожного клієнта.
# Знайдіть максимальну та мінімальну суми замовлень.
# Підрахуйте загальну суму всіх замовлень.

import pandas as pd

df_orders = pd.read_csv("orders.csv")

orders_top_ten = df_orders.head(10)
print("top 10 of orders:")
print(orders_top_ten)

client_orders =df_orders["Клієнт"].value_counts()
print("\nCount of orders each client:")
print(client_orders)

max_sum = df_orders["Сума"].max()
min_sum = df_orders["Сума"].min()
print("\nMax summa of orders = ", max_sum)
print("\nMin summa of orders = ", min_sum)

total_sum = df_orders["Сума"].sum()
print("\nTotal summa of orders = ", total_sum)