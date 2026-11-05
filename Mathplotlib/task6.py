# Дано чотири набори метрик продукту: конверсія, утримання, середній чек, кількість замовлень.
# Потрібно показати їх на окремих панелях.
# Створіть чотири набори числових значень за однією шкалою часу.
# Створіть сітку з чотирьох підграфіків 2х2.
# На кожному підграфіку побудуйте відповідний графік.
# Додайте заголовки для кожного підграфіка та загальний заголовок.
# Відобразіть результат на екрані.

import matplotlib.pyplot as plt
import numpy as np

# 1. Чотири набори числових значень за однією шкалою часу (наприклад, 6 тижнів)
time = ['Тиждень 1', 'Тиждень 2', 'Тиждень 3', 'Тиждень 4', 'Тиждень 5', 'Тиждень 6']
conversion = [2.1, 2.3, 2.0, 2.6, 2.9, 3.2]          # у відсотках
retention = [40, 42, 41, 45, 47, 50]                # у відсотках
average_check = [550, 580, 540, 610, 630, 660]      # у грн
orders_count = [120, 135, 125, 150, 170, 190]       # шт

fig, axs = plt.subplots(2,2, figsize=(12,8))
fig.suptitle('Метрики продукту в динаміці', fontsize=16, fontweight='bold')

axs[0, 0].plot(time, conversion, color='purple', marker='o')
axs[0, 0].set_title('Конверсія (%)')
axs[0, 0].grid(True, linestyle=':', alpha=0.6)
axs[0, 0].tick_params(axis='x', rotation=15)

axs[0, 1].plot(time, retention, color='green', marker='s')
axs[0, 1].set_title('Утримання (Retention, %)')
axs[0, 1].grid(True, linestyle=':', alpha=0.6)
axs[0, 1].tick_params(axis='x', rotation=15)

axs[1, 0].plot(time, average_check, color='blue', marker='^')
axs[1, 0].set_title('Середній чек (грн)')
axs[1, 0].grid(True, linestyle=':', alpha=0.6)
axs[1, 0].tick_params(axis='x', rotation=15)

axs[1, 1].bar(time, orders_count, color='coral')
axs[1, 1].set_title('Кількість замовлень (шт)')
axs[1, 1].grid(axis='y', linestyle=':', alpha=0.6)
axs[1, 1].tick_params(axis='x', rotation=15)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()