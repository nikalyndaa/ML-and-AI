# Дано значення вікових груп 100 осіб. Потрібно показати розподіл.
# Створіть список (або масив) зі 100 цілих значень віку.
# Побудуйте гістограму розподілу.
# Додайте вертикальну лінію середнього значення.
# Підпишіть осі та додайте заголовок.
# Відобразіть графік на екрані.

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
ages = np.random.randint(18,71, size=100)

plt.figure(figsize=(8,5))
plt.hist(ages,bins=10,color="pink", edgecolor="red", alpha=0.7)

avg_age = np.mean(ages)
plt.axhline(avg_age, color="green", linestyle='--',linewidth=2, label=f'Середній вік: {avg_age:.1f} р.')

plt.title('Розподіл віку 100 осіб', fontsize=14)
plt.xlabel("Вік",fontsize=12)
plt.xlabel("Кількість осіб",fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle=':', alpha=0.6)

plt.show()