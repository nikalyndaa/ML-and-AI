# Потрібно проаналізувати взаємозв'язок між користувачами, сесіями та виручкою за днями. Усе
# необхідно запрограмувати в Python з використанням pandas, Numpy i Matplotlib.
# Сформуйте таблицю мінімум на 30 днів із колонками "date", "users", "sessions", "revenue".
# Розрахуйте кореляційну матрицю для цих метрик.
# Побудуйте діаграми розсіювання для пар: users-sessions, users-revenue, sessions-revenue.
# Побудуйте лінійний графік "revenue" за датами.
# Виведіть матрицю та всі графіки.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
dates = pd.date_range("2026-01-01", periods=30)

users = np.random.randint(100,1000,30)

sessions = users * np.random.uniform(1.2,2.5,30)
revenue = sessions * np.random.uniform(5,15,30)

df = pd.DataFrame({
    'date': dates,
    'users' : users,
    'sessions': sessions.astype(int),
    'revenue': revenue.round(2)
})

print(df)

correlation = df[['users', 'sessions', 'revenue']].corr()
print("\n Correlation matrix: ")
print(correlation.round(3))

#  users-session
plt.figure(figsize=(7,5))
plt.scatter(df['users'], df['sessions'], label='Data points')

k, b = np.polyfit(df['users'], df['sessions'],1)
x = np.linspace(df['users'].min(), df['users'].max(), 100)
y = k*x + b
plt.plot(x,y, color='red', label='Trend line')
plt.title("Depends between users snd sessions")
plt.xlabel('Users')
plt.ylabel('Sessions')
plt.legend()
plt.grid()
plt.show()