# syntax

def sum(a, b):  # define a function
    sum = a + b  # statement
    print(sum)  # output of the statement


sum(5 + 9, 6)  # call the function


def multiplication_division(a, b):
    multi = a * b
    divi = a / b
    return multi, divi


multiplication, division = multiplication_division(int(input("enter a first number")), 5)   # if need two outupt then for save two output need two variables also
print("multiplication is :", multiplication, "and division of numbers is :", division)
