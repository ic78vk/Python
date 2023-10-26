# import switch as switch
#
# from array import *
# a=array('i',[])
# len=int(input("enter a length of array"))
# # def addin(x):
# #     a.append(x)
# #     return a
# # for i in range(2):
# #
# #
# #     }
# #
# # b=int(input('enter a number'))
# # addin(b)
# # print(f'array after inster {b} :', a)
# # print(a)
#
# for i in range(len):
#     val=int(input("enter a next value"))
#     a.append(val)
#
# print(a)
# k=0
# serch=int(input("enter a value to sarch"))
# for e in a:
#     if e==serch:
#         print(k)
#         break
#     k+=1
# else:
#     print("enter a valid number")
from array import *
arr=array('i',[])
leng=int(input("enter a lenght of array"))
for i in range(leng):
    val=int(input("enter a next value"))
    arr.append(val)
print(arr)
for i in range(len(arr)):
    print(f'{i+1} element of array is ',arr[i])
k=0
serch=int(input("enter a value to search "))
for e in arr:
    if e==serch:
        print("your serach value presend in index number of array",k)
        ans=int(input('did you want to delete searched value (reply 1 for yes and 2 for no)?'))
        if ans == 1:
            deleted = arr[k]
            print("temp deleted value", deleted)
            arr.remove(e)
            print(f"after deleting {deleted} value update array is :", arr)
            break
        break
    k+=1
else:
    print("enter a valid number")