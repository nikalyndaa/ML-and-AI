# Потрібно проаналізувати дані А/В-експерименту та візуалізувати конверсії. Усе необхідно
# запрограмувати в Python з використанням pandas, NumPy i Matplotlib.
# Сформуйте таблицю з полями "group" (A або В) і "converted" (0/1) з не менш ніж 100
# спостереженнями в кожній групі.
# Розрахуйте конверсію в групах, абсолютну різницю та відносну зміну.
# Побудуйте 95% довірчі інтервали для конверсії в кожній групі.
# Побудуйте стовпчасту діаграму конверсій груп із відображенням довірчих інтервалів.
# Виведіть усі розраховані значення та графік.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n=200

group_a= np.random.binomial(1,0.10,n)
group_b= np.random.binomial(1,0.15,n)

df = pd.DataFrame({
    'group': ['A'] * n + ['B'] * n,
    'converted': np.concatenate([group_a, group_b])
})

print("Таблиця A/B-експерименту:")
print(df)

conversion_a = df[df['group'] == 'A']['converted'].mean()
conversion_b = df[df['group'] == 'B']['converted'].mean()

print("\nКонверсія групи A:", round(conversion_a * 100, 2), "%")
print("Конверсія групи B:", round(conversion_b * 100, 2), "%")

absolute_difference = conversion_b - conversion_a

print("Абсолютна різниця:",
      round(absolute_difference * 100, 2), "відсоткових пунктів")

relative_change = (conversion_b - conversion_a) / conversion_a

print("Відносна зміна:",
      round(relative_change * 100, 2), "%")

def confidence_interval(data):
    n = len(data)
    p = np.mean(data)

    z = 1.96

    error = z * np.sqrt(p * (1 - p) / n)

    lower = p - error
    upper = p + error

    return lower, upper


ci_a = confidence_interval(group_a)
ci_b = confidence_interval(group_b)

print("\n95% довірчий інтервал групи A:")
print(round(ci_a[0] * 100, 2), "% -",
      round(ci_a[1] * 100, 2), "%")

print("\n95% довірчий інтервал групи B:")
print(round(ci_b[0] * 100, 2), "% -",
      round(ci_b[1] * 100, 2), "%")

# 7. Побудова стовпчастої діаграми
conversions = [conversion_a * 100, conversion_b * 100]

lower_errors = [
    (conversion_a - ci_a[0]) * 100,
    (conversion_b - ci_b[0]) * 100
]

upper_errors = [
    (ci_a[1] - conversion_a) * 100,
    (ci_b[1] - conversion_b) * 100
]

errors = np.array([lower_errors, upper_errors])

plt.figure(figsize=(8, 5))

plt.bar(
    ['Group A', 'Group B'],
    conversions,
    yerr=errors,
    capsize=8
)

plt.title('Порівняння конверсій груп A та B')
plt.xlabel('Група')
plt.ylabel('Конверсія (%)')
plt.grid(axis='y')

plt.show()