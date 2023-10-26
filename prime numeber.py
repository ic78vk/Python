num=int(input("enter a number"))
for i in range(2,num):
    if num%i==0:
        print(f"Entered number {num} is a prime number")
        break
else:
    print(f"Entered number {num} is a prime number")