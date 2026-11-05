# € денні значення температури та вологості за тиждень. Потрібно показати обидві метрики на
# загальній діаграмі.
# Створіть список дат (7 днів) і два списки значень: температура і вологість.
# Побудуйте лінійний графік температури.
# На тій самій області побудуйте графік вологості.
# Додайте легенду, підписи осей і заголовок.
# Поверніть підписи дат на осі X для читабельності та відобразіть графік.
import matplotlib.pyplot as plt
dates = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд']
temperature = [22, 24, 19, 21, 25, 27, 26]
humidity = [65, 60, 80, 75, 55, 50, 53]

fig, ax1 = plt.subplots(figsize=(9, 5))
color = 'tab:red'
ax1.set_xlabel('Дні тижня', fontsize=12)
ax1.set_ylabel('Температура (°C)', color=color, fontsize=12)
line1 = ax1.plot(dates, temperature, color=color, marker='o', linewidth=2, label='Температура')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Вологість (%)', color=color, fontsize=12)
line2 = ax2.plot(dates, humidity, color=color, marker='s', linestyle='--',linewidth=2, label='Вологість')
ax2.tick_params(axis='y', labelcolor=color)

lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')
plt.title('Денні значення температури та вологості за тиждень', fontsize=14)
plt.xticks(rotation=45)
ax1.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.show()