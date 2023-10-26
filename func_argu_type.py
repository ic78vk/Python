def person(name, mobile, age=22,):
    print(name)
    print(age)
    print(mobile)
person('rahul',age=36,mobile=4454821268)

print("this is 2nd program")
def sum(a,*v):
    c=a
    for i in v:
        c=c+i
    print("sum is :",c)
sum(558,6,9)

def sum2(*a):
    d=0
    for i in a:
        d=d+i
    print(f"sum of *a is {d}")
sum2(int(input("enter 1st number")),75,75,50,96+4)