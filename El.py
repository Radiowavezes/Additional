def average_num(myList):
    s = 0
    a = 0
    for i in myList:
        s += i
        a += 1
    return s / a



myList = list(map(int, input().split()))
print(average_num(myList))
