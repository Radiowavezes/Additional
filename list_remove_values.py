import random


def initi(i, li):
    while i in li:
        li.remove(i)
    else:
        return li


n = None
myList = []
while n != 0:
    try:
        n = int(input('Enter the num from 1 to 9. To stop enter 0: '))
        if n != 0:
            myList.append(n)
    except ValueError:
        continue
num = random.choice(range(1, 10))
print(num)
print(myList)
print(initi(num, myList))
