# Потрібно проаналізувати часовий ряд продажів і візуалізувати ковзаючі метрики. Усе необхідно
# запрограмувати в Python з використанням pandas, Numpyi Matplotlib.
# Сформуйте таблицю "date" i "sales" за 90 днів.
# Додайте ковзне середнє і ковзне стандартне відхилення за обраним вікном.
# Побудуйте графік вихідних продажів і графік ковзного середнього на одному полі.
# Побудуйте окремий графік ковзного стандартного відхилення.
# Виведіть таблицю з першими рядками нових стовпців і обидва графіки.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
dates = pd.date_range(
    start='2026-01-01',
    periods=90
)
sales = np.random.normal(
    loc=1000,
    scale=150,
    size=90
)
sales = np.maximum(sales, 0).round(2)

df = pd.DataFrame({
    'date': dates,
    'sales': sales
})

print("Початкова таблиця:")
print(df)

window = 7

df['rolling_mean'] = df['sales'].rolling(
    window = window
).mean().round(3)

df['rolling_std'] = df['sales'].rolling(
    window=window
).std().round(3)

print("\nТаблиця з ковзними метриками:")
print(df[['date', 'sales', 'rolling_mean', 'rolling_std']].head(15))

plt.figure(figsize=(12,5))
plt.plot(df['date'],
         df['sales'],
         label='Sales',
         alpha=0.6)

plt.plot(
    df['date'],
    df['rolling_mean'],
    label='Rolling Mean',
    linewidth=2
)


plt.title('Продажі та ковзне середнє за 90 днів')
plt.xlabel('Дата')
plt.ylabel('Продажі')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()

plt.show()

plt.figure(figsize=(12, 5))

plt.plot(
    df['date'],
    df['rolling_std'],
    label='Rolling Standard Deviation'
)

plt.title('Ковзне стандартне відхилення продажів')
plt.xlabel('Дата')
plt.ylabel('Стандартне відхилення')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()

plt.show()