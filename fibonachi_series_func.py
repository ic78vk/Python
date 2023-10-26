import sys

# lim=int(input("enter a max recursion limit"))
sys.setrecursionlimit(31)  # should be equal or more than to 31
# sys.setrecursionlimit(330)


def fib(n):
    if sys.getrecursionlimit() <= n:
        print("please enter the number below recursion limit", sys.getrecursionlimit())
    else:
        a = 0  # common for negative and positive number series
        b = 1  # used only in Positive number series (Grater than 0)
        e = -1  # used only in Negative number series (less than 0)
        if n == 1 or n <= 0:
            if n == 1:
                print(a)
            elif n <= 0:
                print("Fibonacci series for Negative numbers")
                print(a)
                print(e)
                for i in range(-2, n, a + e):  # if user want series in negative numbers
                    c = a + e
                    a = e
                    e = c
                    print(c)
        else:
            print("Fibonacci series for Positive numbers")
            print(a)
            print(b)
            for i in range(2, n):
                c = a + b
                a = b
                b = c
                print(c)


fib(int(input("enter a number")))
