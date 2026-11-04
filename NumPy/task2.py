import numpy as np

num1 = int(input("enter 1 number: "))
num2 = int(input("enter 2 number: "))

# create matrix using user numbers
matrix= np.random.randint(num1,num2+1, size=(5,5))
print("\nMatrix:")
print(matrix)

# get main diaagonal
diagonal_elem = np.diagonal(matrix)
print("\nElements of main diagonal: ",diagonal_elem)

sum_of_diagonal_elem = sum(diagonal_elem)
print(f"Summa of diagonal elements = {sum_of_diagonal_elem}")

modified_matrix = np.tril(matrix)
print(modified_matrix)