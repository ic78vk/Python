from numpy import *
from array import *
arr1=array('i',[55,478,5,4,3,31])
arr2=array('i',[556,96,3,52,368,65])
# print("arr1[2] is :", arr1[2])
# print("arr2[6] is: ",arr2[4])
# name=arr1[2]+arr2[4]
# print(f"addition of {arr1[2]} and {arr2[4]} is ",name)
# print(type(name))
# type(arr1)
# arr3=array('i',[])

# ## problem add 2 array values in one array using for loop

arr3=array('i',[])
print(len(arr3))
for i in range(len(arr1)):
    arr3.append(arr1[i]+arr2[i])
print(arr3,"length of array is :", len(arr3))

# ## problem print max number present in array without using prebuilt function

max=0
for i in range(len(arr3)):
    print(f"in {i} iteration value of i is: ",arr3[i])
    if arr3[i]> max:
        max=arr3[i]
print(max)