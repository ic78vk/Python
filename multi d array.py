# import numpy#numpy not available by default ; user have to install it using pip3 install numpy
from numpy import *

# arr=array([2,5,5,6,8,3,2,4,8,6],[2,5,6,3,6,9,4,5,5,8,3])
# print(arr)
# types of declaration array using Numpy in python

print("types of declaration array using Numpy in python")

arr2 = linspace(0, 15, 6)
print("this is the out put of lin space() arrays", arr2)

arr3 = logspace(1, 15, 3)
print("this is the out put of logspace() arrays: ", arr3)

arr4 = arange(1, 15, 3)
print("this is output of arrange array", arr4)

arr5 = zeros(5)
print("this is the output of Zeros() arrays", arr5)

arr5 = ones(10)
print("this is the output of ones() array", arr5)
