a = 12
print("id of a ", id(a))  # globle variables
b = 32
print("id of b ", id(b))  # globle variables
c = 45
print("id of c ", id(c))  # globle variables


def sample():
    a = 33  # create local variables
    print("id of a ", id(a), a)  # local variables
    x = globals()['b']
    print(f"id of x {id(x)}, {x}")
    y = globals()['a']  # calling and store globle variable a into y
    print(f"id of y {id(y)} ,{y}")
    print(f"id of local a {id(a)}  {a}")
    # print(id(x), id(a))
    globals()['b'] = 55  # Changing the value of globle variable b from 32  to 55


sample()

print(f"id of globle variable a is {id(b)} and value of a is {b}")
