def update(x):
    print("this is a default value of x before excuting the function :", x, " id of x is ", id(x))
    # x=int(input("enter a new value of x"))
    x[1],x[2] = [int(input("enter a value")), int(input("enter 2nd value"))]
    print("after updating x is", x, " id of x after updateing is :", id(x))


val = [25, 36, 33]
print(f"value of x is {val} and id of x is {id(val)}")
update(val)
print(f"after updating this value of val is : {val} and id of val is {id(val)}")
