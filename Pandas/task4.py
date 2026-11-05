# Зібрано дані про співробітників та їхні проекти: "/м'я", "Проект", "Години".
# 이
# Створіть DataFrame з не менш ніж вісьмома рядками.
# Виведіть вихідний DataFrame.
# Підрахуйте загальну кількість годин за кожним співробітником.
# Підрахуйте загальну кількість годин за кожним проектом.
# Знайдіть співробітника, який витратив найбільше годин.
import pandas as pd

emp_data = {
    "Ім'я": ["Андрій", "Олена", "Андрій", "Максим", "Олена", "Ірина", "Максим", "Ірина"],
    "Проект": ["Alpha", "Beta", "Gamma", "Alpha", "Gamma", "Beta", "Beta", "Alpha"],
    "Години": [15, 20, 10, 25, 30, 12, 18, 22]
}

df_data = pd.DataFrame(emp_data)
print("DataFrame of employee")
print(df_data)

hours_per_emp = df_data.groupby("Ім'я")["Години"].sum()
print("\nTotal sum of hour per employee")
print(hours_per_emp)

hours_per_proj = df_data.groupby("Проект")["Години"].sum()
print("\nTotal sum of hour per project")
print(hours_per_proj)

top_employee = hours_per_emp.idxmax()
print(f"\nEmployee with max hours: {top_employee}")