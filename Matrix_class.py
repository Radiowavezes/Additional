from sys import stdin

from copy import deepcopy as dc


class Matrix:
    def __init__(self, li):
        self.li = dc(li)

    def __str__(self):
        res = ""
        for row in self.li:
            line = "\t".join([str(symbol) for symbol in row])
            res += line + "\n"
        return res[:-1]

    def size(self):
        return len(self.li), len(self.li[0])

    def __add__(self, next):
        res = []
        for i, j in zip(self.li, dc(next.li)):
            row = []
            for n, m in zip(i, j):
                row.append(m + n)
            res.append(row)
        return Matrix(res)

    def __mul__(self, n):
        res = []
        for i in self.li:
            row = []
            for j in i:
                row.append(j * n)
            res.append(row)
        return Matrix(res)

    __rmul__ = __mul__


exec(stdin.read())
