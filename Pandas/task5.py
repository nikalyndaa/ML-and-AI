# У вас є таблиця продажів квитків: "Фільм", "Місто", "Продані квитки".
# Створіть DataFrame з не менш ніж дванадцятьма рядками.
# Виведіть увесь DataFrame.
# Підрахуйте загальну кількість проданих квитків за кожним фільмом.
# Підрахуйте загальну кількість квитків по кожному місту.
# Знайдіть фільм із найбільшою кількістю продажів.

import pandas as pd

tickets_data = {
    "Фільм": ["Аватар 2", "Дюна 2", "Аватар 2", "Барбі", "Оппенгеймер", "Дюна 2",
              "Барбі", "Оппенгеймер", "Аватар 2", "Дюна 2", "Барбі", "Оппенгеймер"],
    "Місто": ["Київ", "Київ", "Львів", "Львів", "Одеса", "Одеса",
              "Харків", "Харків", "Харків", "Львів", "Київ", "Одеса"],
    "Продані квитки": [450, 300, 200, 350, 150, 280, 400, 190, 220, 310, 500, 170]
}

df_data = pd.DataFrame(tickets_data)
print(df_data)

tickets_per_movie = df_data.groupby("Фільм")["Продані квитки"].sum()
print("\nTickets per movie: ")
print(tickets_per_movie)

tickets_per_city = df_data.groupby("Місто")["Продані квитки"].sum()
print("\nTickets per city: ")
print(tickets_per_city)

top_movie = tickets_per_movie.idxmax()
top_movie_sales = tickets_per_movie.max()
print(f"\nTop movie: {top_movie} - {top_movie_sales}")