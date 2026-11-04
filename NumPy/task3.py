import numpy as np

num_start = int(input("enter start number: "))
num_end = int(input("enter end number: "))

if (num_end - num_start+1)!=30:
    print("error! count of numbers must be 30")
else:
    sequence = np.arange(num_start, num_end+1)

    matrix = sequence.reshape(6,5)
    print("\nOne matrix:")
    print(matrix)

    # count sum of each rows
    row_sums = np.sum(matrix,axis=1)
    print("\nMatrix of sum in each rows:")
    print(row_sums)

    col_max = np.max(matrix,axis=0)
    print("\nMatrix of max in each cols:")
    print(col_max)