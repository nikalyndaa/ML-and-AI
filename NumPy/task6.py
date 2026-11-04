import numpy as np

n = int(input("enter count of rows: "))
m = int(input("enter count of cols: "))
total_el = n * m
matrix = np.arange(1,total_el+1).reshape(n,m)
print("\nMatrix:")
print(matrix)

new_n =int(input("enter count of new rows: "))
new_m =int(input("enter count of new cols: "))
new_matrix = matrix.reshape(new_n,new_m)
print("\nNew Matrix with new(n*m):")
print(new_matrix)

# Визначте мінімальні та максимальні значення в кожному рядку нової матриці та виведіть
# обидва одновимірні масиви.
min_rows = np.min(new_matrix,axis=1)
max_rows = np.max(new_matrix,axis=1)

print("\nMin elem in rows: ", min_rows)
print("\nMax elem in rows: ", max_rows)

# Підрахуйте загальну суму всіх елементів нової матриці та виведіть результат.
total_sum = np.sum(new_matrix)
print("\nTotal sum elems in matrix = ", total_sum)