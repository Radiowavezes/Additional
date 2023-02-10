from itertools import permutations, combinations
import time

def find_terms(terms, target):
    left = round((sum(terms) - target), 2)
    if left in terms:
        terms.remove(left)
        return f'{terms} matching {target} is {round(sum(terms), 2) == target}'
    i = 2
    while i != len(terms):
        ammount = combinations(terms, i)
        for j in ammount:
            print(j)
            if round(sum(j), 2) == target:
                return f'{j} matching {target} is {round(sum(j), 2) == target}'
            elif round(sum(j), 2) == left:
                for num in j:
                    terms.remove(num)
                print(round(sum(terms), 2))
                print(target)
                print(round(sum(terms), 2) == target)
                return f'{terms} matching {target} is {round(sum(terms), 2) == target}'
        i += 1
    return f'No match'

with open('D:\Babenko\Beetroot\\additional\Other\\bank_new.txt', 'r+') as file:
    tg = (file.readline())
    mytable = tg.maketrans(",", ".")
    target = float(tg.translate(mytable))
    file.readline()
    terms = [float(line.strip().translate(mytable)) for line in file]
    start = time.time()
    print(find_terms(terms, target))
    print(round((time.time() - start) // 60), 'minutes', round((time.time() - start) % 60), 'seconds')