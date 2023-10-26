num=int(input('enter a number : '))
while(num>=0):
    print("rahul", end=" ")
    j=1
    while(j<=5):
        print("khanna", end=" ")
        j +=1
    j=j+1
    num= num-1
    print()

def rahul(a,b):
    print(a+b)
    return (a+b)
g=int(input('enter a number'))
f=int(input('enter a number'))
print(f'adition of {g} and {f} is : ',rahul(g,f))