# numberss=[20,45,78,42187,4487,10,4841,121,521,2154,15,54,1154,33,84,1548,154,88]
# for num in numberss:
#     if num%2==0:
#         print(num)
#     else:
#         break
# else :
#     print('Not any number found')
import math
import random
min=int(input('enter a minimum limit'))
max=int(input('Enter a maximum limit'))
num1=random.randint(min,max)
print(num1)
while (num1 >= 0):
    a=int(input("enter a number again"))
    if num1 == a:
        print(f"your entered number {num1} is match with random genrated number {num1}")
        exit()
    elif num1 > a and a > min or a < max:
        print(f"Your entered number {a} is less to the genrated number")
    elif num1 < a and a > min or a < max:
        print(f'Your entered number {a} is Greater than to the genrated number')
    else:
        print(f"Enter valid number between {min} to {max}")