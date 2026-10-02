import numpy as np

# arr = np.array([10,20,30,40,50,60])
# print(arr[4:])
# print(arr[:4])



arr = np.array([10,20,30,40,50,60])
filterr = arr[arr%3 == 0]
print(filterr)
 
