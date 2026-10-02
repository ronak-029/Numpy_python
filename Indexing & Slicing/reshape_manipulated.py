import numpy as np

# arr = np.array([1,2,3,4])

# new_arr = np.insert(arr,2,9)
# print(new_arr)
# print(arr)

# arr = np.array([[1,2],[3,4]])

# new_arr = np.insert(arr , 1 ,[5,6],axis=1)
# print(new_arr)


# Apped
# arr = np.array([1,2,3,4])
# new_arr = np.append(arr,7)
# print(new_arr)

# concatenate
# arr1 = np.array([1,2])
# arr2 = np.array([2,4])
# new_arr = np.concatenate((arr1,arr2))
# print(new_arr)

# delete function
# arr = np.array([1,2,3,4])
# new_arr = np.delete(arr,2)
# print(new_arr)


arr = np.array([[1,2],[3,4],[5,6]])
new_arr = np.delete(arr , 0 ,axis=1)
print(new_arr)

