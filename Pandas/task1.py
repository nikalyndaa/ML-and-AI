# У вас є дані про книги з полями: "Назва", "Автор", "Рік видання", "Ціна".
# Створіть Data Frame з не менш ніж шістьма рядками.
# Виведіть увесь DataFrame.
# Визначте середню ціну книг.
# Знайдіть книги, видані після 2015 року.
# Відсортуйте Data Frame за ціною в порядку зростання.
import pandas as pd
data = {
    "Назва": ["Кобзар", "1984", "Тіні забутих предків", "Алхімік", "Маленький принц", "Флагмани", "Інтермеццо"],
    "Автор": ["Тарас Шевченко", "Джордж Орвелл", "Михайло Коцюбинський", "Пауло Коельйо", "Антуан де Сент-Экзюпері", "Володимир Винниченко", "Михайло Коцюбинський"],
    "Рік видання": [1840, 1949, 1911, 1988, 1943, 2020, 1908],
    "Ціна": [250, 320, 180, 290, 210, 450, 160]
}

df_books = pd.DataFrame(data)

print("DataFrame of books: ")
print(df_books)

avg_price = df_books["Ціна"].mean()
print(f"Avarage of privce = {avg_price:.2f}")

collection_books_year = df_books[df_books["Рік видання"] > 2015]
print(f"\nBooks published after 2015: {collection_books_year}")

sort_books = df_books.sort_values("Ціна", ascending=True)
print("\nSorted books by price:")
print(sort_books)
