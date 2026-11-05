# Є погодинні дані навантаження сервера за добу. Потрібно показати зміни і виділити область між
# кривою і віссю Х.
# Створіть список годин (0-23) і відповідні значення навантаження.
# Побудуйте лінійний графік навантаження.
# Зафарбуйте область під кривою.
# Додайте сітку, підписи осей і заголовок.
# Відобразіть графік на екрані.

import matplotlib.pyplot as plt

hours = list(range(24))
load = [15, 10, 8, 5, 6, 12, 25, 45, 70, 85, 90, 88,
        75, 80, 82, 78, 85, 95, 90, 70, 55, 40, 30, 20]

plt.figure(figsize=(10,5))
plt.plot(hours,load, color='darkorange', linewidth=2, marker='o', label="Навантаження (%)")
plt.fill_between(hours,load, color='orange', alpha=0.3)

plt.title('Погодинне навантаження сервера за добу', fontsize=14)
plt.xlabel('Година доби', fontsize=12)
plt.ylabel('Навантаження', fontsize=12)
plt.xticks(hours)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.tight_layout()
plt.show()