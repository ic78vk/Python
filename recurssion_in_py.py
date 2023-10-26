import sys
sys.setrecursionlimit(2000)
i=0
def welcome():
    global i
    i +=1
    print("hello", i)
    welcome()
welcome()