# CHECK the user entered number is -ve or +ve
# take user input and show gretest input number among them

number=int(input("enter a numnber : "))
a=int(input(" enter a 1st numnber"))
b=int(input(" enter a 2nd numnber"))
c=int(input(" enter a 3rd numnber"))

# if (number>=0):
#     print(f'Entered number {number} is a positive number')
# else:
#     print(f'Entered number {number} is a Nigative number')
# exit()

if(a>=b and a>=c):
    print(f'{a} is a greatest number from {a}, {b}, {c}')
elif(b>=a and b>=c):
    print(f'{b} is the greater number from {a}, {b}, {c}')
elif(c>=a and c>=b):
    print(f'{c} is the greater number from {a,b,c}')
else:
    print('enter a valid number')
exit()