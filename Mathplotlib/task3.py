# Є результати іспитів за трьома групами студентів. Потрібно порівняти розкид оцінок між групами.
# 이
# Створіть три набори числових результатів (по одній вибірці на групу).
# Побудуйте графік boxplot для трьох груп поруч.
# Підпишіть групи по осі X.
# Додайте підписи осей і заголовок.
# Відобразіть графік на екрані.

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
group_a = np.random.normal(75, 10, size=30)
group_b = np.random.normal(82, 8, size=30)
group_c = np.random.normal(68, 15, size=30)

data_to_plot = [group_a, group_b, group_c]
groups_labels = ['Група А', 'Група Б', 'Група В']

plt.figure(figsize=(8, 5))
plt.boxplot(data_to_plot,tick_labels=groups_labels,patch_artist=True,
            boxprops=dict (facecolor='lightgreen', color='darkgreen'),
            medianprops=dict (color='red', linewidth=2))

plt.title('Порівняння розкиду оцінок між групами студентів', fontsize=14)
plt.xlabel('Студентські групи', fontsize=12)
plt.ylabel('Оцінки', fontsize=12)
plt.grid(axis='y', linestyle=':', alpha=0.6)

# 4. Відображення графіка
plt.show()