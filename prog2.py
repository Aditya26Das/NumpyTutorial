import numpy as np


# Creating an ndarray. Array object in numpy is called ndarray
# x = np.array([1,2,3])
# y = np.array({"name": "Aditya", "surname": "Das", "age": 19,})
# z = np.array((1,2,3.5,5))
# print(x)
# print(y)
# print(z)


#Dimensions in array. A dimension in an array is one level of array depth (nested array)

# 0-D array : or scalars are the elements in array, each value in an array is 0-D.
#Now we will create a 0-D array.
# a = np.array(42)
# print(a)

# 1-D array : an array that has 0-D array as its element is called 1-D array
# x = np.array([1,2,3,4,5])
# print(x)

# 2-D array : containing two arrays with certain values
# y = np.array([[1,2,3],["Adi","Das","Me"]])
# print(y)

# 3-D array : contains two 2-D arrays
# z = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(z),

# Check how many dimensions the array has: ndim attribute
# d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(d.ndim)


#Create an array of 5 dimensions and verify that it has 5 dimensions.
# e = np.array([[[[[1],[2]],[[3],[4]],[[5],[6]],[[7],[8]],[[9],[10]],[[11],[12]]]]])
# print(e.ndim)

#Convert 1-D to 5-D.
f = np.array([1,2,3,4,5],ndmin = 5)
print(f)
print(f.ndim)