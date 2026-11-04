import numpy as np

arr = np.random.randint(0,51,size=20)
print("Масив: ")
print(arr)

user_num =int(input("\Введіть порогове значення: "))

res_comp = np.sum(arr>user_num)
print(
    f"Кількість елементів більших за {user_num}: {res_comp}"
)

max_val = np.max(arr)
max_index = np.argmax(arr)
print(f"Максимальне значення: {max_val} (позиція першої появи: {max_index})")

sorted_arr_des = np.sort(arr)[::-1]
print(sorted_arr_des)