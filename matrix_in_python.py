from numpy import *

arr1 = array([12, 15, 56, 58, 11, 22, 36, 13, 44, 39, 85, 99])
print(arr1)
print(arr1, "dia-mentions of arr2 is ", arr1.ndim)

arr2 = arr1.reshape(2, 2, 3)
print(arr2, " and diamentions of arr2 is: ", arr2.ndim)

arr4 = array([[3, 1, 2, 5, 6, 9],
              [15, 23, 39, 44, 56, 65],
              [923, 456, 963, 368, 264, 166]])
print(arr4, " diamantions of arr4 is :", arr4.ndim)
