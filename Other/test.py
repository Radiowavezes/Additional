from math import factorial as f
from itertools import combinations

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

c = f(len(l)) / (f(3) * f(len(l) - 3))
sum = 0
for j in combinations(l, 3):
    sum += 1
print(sum==c)