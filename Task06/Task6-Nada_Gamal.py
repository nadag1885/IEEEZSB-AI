import numpy as np
#problem1
arr = np.diag([9, 9, 9])
print(arr)
print("#"*50)

#problem2
arr=np.arange(2,33,2)
print(arr.reshape(4,4))
x1=arr.mean()-0.5*arr.std()
x2=arr.mean()+0.5*arr.std()
arr1=arr[arr>x1]
arr2=arr1[arr1<x2]
print(arr2)
print("#"*50)

#problem3
arr=np.zeros((9,9))
print(arr)
print("#"*50)

#problem4
arr=np.ones((4,4))+np.arange(4)
print(arr)
print("#"*50)

