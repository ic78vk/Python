def count(x):
    even = 0
    odd = 0
    for i in x:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


i = int(input("how many number u want to enter"))
lst = []
for i in range(i):
    print("correct values in list", lst)
    val = int(input("enter the next number"))
    lst.insert(i, val)
list2 = [12, 36, 25, 45, 75, 95, 66, 31, 67]
even, odd = count(lst)
print(f"even : {even}, odds : {odd}",f"length of list is {len(lst)}",f"length of temp list is : {len(list2)}")
