import numpy as np

lenght = int(input("enter lenght of arr: "))

arr1 = np.random.randint(0,11,lenght)
arr2 = np.random.randint(10,21,lenght)

print("\nfirst arr: ",arr1)
print("\nsecond arr: ",arr2)

new_arr = np.concatenate((arr1,arr2))
print("\nconcatenated arrays: ", new_arr)

elem_add = arr1 + arr2
elem_sub = arr1-arr2

print("\nelem add of two arrays:",elem_add)
print("\nelem sub of two arrays:",elem_sub)