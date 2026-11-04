import numpy as np

num1 = int(input("enter 1 number: "))
num2 = int(input("enter 2 number: "))

# create matrix using user numbers
array= np.random.randint(num1,num2+1, size=15)
print("\nArray:")
print(array)

neg_arr = array[array<0]
print("\nNegative elements of array: ", neg_arr)

modify_arr = np.copy(array)
modify_arr[modify_arr<0]=0
print("\nModified arr with zeros: ", modify_arr)

count_of_zeros = np.sum(modify_arr==0)
print("\ncount zeros in modified array", count_of_zeros)