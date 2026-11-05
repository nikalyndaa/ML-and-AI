# Є таблиця з даними про продукти харчування: "Продукт", "Категорія", "Калорії", "Білки".
# 이
# Створіть DataFramе з не менш ніж десятьма рядками.
# Виведіть увесь Data Frame.
# Знайдіть усі продукти з калорійністю вище 300.
# Підрахуйте середню кількість білків за категоріями.
# Відсортуйте Data Frame за калорійністю в порядку убування.

import pandas as pd

food_data = {
    "Продукт": ["Яблуко", "Куряча грудка", "Шоколад", "Рис", "Лосось", "Сир твердий", "Горіхи волоські", "Банан", "Вівсянка", "Авокадо"],
    "Категорія": ["Фрукти", "М'ясо", "Солодощі", "Крупи", "Риба", "Молочні", "Горіхи", "Фрукти", "Крупи", "Фрукти"],
    "Калорії": [52, 165, 546, 130, 208, 402, 654, 89, 370, 160],
    "Білки": [0.3, 31.0, 4.9, 2.7, 20.0, 25.0, 15.2, 1.1, 13.0, 2.0]
}

df_food = pd.DataFrame(food_data)

print("DataFrame of products:")
print(df_food)

calories_food = df_food[df_food["Калорії"] > 300]
print("\nProducts with calories over 300: ")
print(calories_food)

avg_protein = df_food.groupby("Категорія")["Білки"].mean().round(2)
print("\nСередня кількість білків за категоріями:")
print(avg_protein)

sort_products = df_food.sort_values("Калорії", ascending=False)
print("\nSorted by desc calories: ")
print(sort_products)
