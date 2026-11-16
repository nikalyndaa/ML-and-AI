# Потрібно перевірити дію центральної граничної теореми на прикладі несиметричного розподілу.
# Усе необхідно запрограмувати в Python з використанням pandas, NumPy i Matplotlib.
# 이
# Згенеруйте генеральну сукупність щонайменше з 50 000 спостережень із несиметричного
# розподілу.
# Сформуйте кілька підвибірок фіксованого розміру п і для кожної обчисліть середнє.
# Збережіть вибіркові середні та побудуйте їхню гістограму.
# Повторіть процедуру для щонайменше двох різних в і виведіть обидві гістограми.
# Виведіть середнєі стандартне відхилення вибіркових середніх для кожного п.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

population = np.random.exponential(
    scale=10,
    size=50000
)

print("Розмір генеральної сукупності:", len(population))
print("Середнє генеральної сукупності:", round(np.mean(population), 2))
print("Стандартне відхилення:", round(np.std(population), 2))


def sample_means(population, n, repetitions=5000):
    means = []
    for i in range(repetitions):
        sample = np.random.choice(
            population,
            size = n,
            replace = True
        )

        means.append(np.mean(sample))

    return np.array(means)

# n=5
means_5 = sample_means(population, 5)
# n=30
means_30 = sample_means(population, 30)

results = pd.DataFrame({
    'mean_n5': means_5,
    'mean_n30': means_30
})

print(results.head())

plt.figure(figsize=(8,5))
plt.hist(means_5, bins=40, density=True, edgecolor='black')

plt.title('Розподіл вибіркових середніх (n = 5)')
plt.xlabel('Вибіркове середнє')
plt.ylabel('Щільність')
plt.grid()
plt.show()

plt.figure(figsize=(8,5))
plt.hist(means_30, bins=40, density=True, edgecolor='black')

plt.title('Розподіл вибіркових середніх (n = 30)')
plt.xlabel('Вибіркове середнє')
plt.ylabel('Щільність')
plt.grid()
plt.show()


print("\n results for n =5:")
print("Середнє", round(np.mean(means_5),3))
print("Стандартне відхилення:", round(np.std(means_5), 3))

print("\n results for n = 30:")
print("Середнє:", round(np.mean(means_30), 3))
print("Стандартне відхилення:", round(np.std(means_30), 3))
