# Дано дві таблиці: перша з інформацією про клієнтів ("ID", "/м'я", "Місто"), друга — з їхніми
# замовленнями ("ID клієнта", "Замовлення", "Вартість").
# Створіть два Data Frameі заповніть їх не менш ніж п'ятьма рядками кожен.
# Виведіть обидва Data Frame.
# Об'єднайте їх за ідентифікатором клієнта.
# Підрахуйте загальну вартість замовлень за кожним клієнтом.
# Виведіть результат у вигляді нового DataFrame.

import pandas as pd

customers_data = {
    "ID": [1, 2, 3, 4, 5],
    "Ім'я": ["Олег", "Анна", "Віктор", "Софія", "Денис"],
    "Місто": ["Київ", "Львів", "Одеса", "Харків", "Дніпро"]
}
df_customers = pd.DataFrame(customers_data)

orders_data = {
    "ID клієнта": [1, 2, 1, 3, 4, 2, 5],
    "Замовлення": ["Телефон", "Ноутбук", "Чохол", "Мишка", "Монітор", "Навушники", "Клавіатура"],
    "Вартість": [12000, 28000, 500, 800, 9000, 2500, 1500]
}
df_orders_info = pd.DataFrame(orders_data)

print("\nTable of customers:")
print(df_customers)

print("\nTable of orders:")
print(df_orders_info)

df_merged = pd.merge(df_orders_info, df_customers, left_on="ID клієнта", right_on="ID")
df_summary = df_merged.groupby(["Ім'я", "Місто"])["Вартість"].sum().reset_index()

df_summary = df_summary.rename(columns={"Вартість": "Загальна вартість замовлень"})
print(df_summary)