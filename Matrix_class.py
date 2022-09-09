from sys import stdin

from copy import deepcopy as dc


class MatrixError(BaseException):
    def __init__(self, Matrix, next):
        self.matrix1 = Matrix
        self.matrix2 = next


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
        if len(self.li) == len(next.li) and len(self.li[0]) == len(next.li[0]):
            for i, j in zip(dc(self.li), dc(next.li)):
                row = []
                for n, m in zip(i, j):
                    row.append(m + n)
                res.append(row)
        else:
            raise MatrixError(self, next)
        return Matrix(res)

    def __mul__(self, next):
        res = []
        if isinstance(next, int):
            for i in dc(self.li):
                row = []
                for j in i:
                    row.append(j * next)
                res.append(row)
        elif isinstance(next, Matrix):
            if (
                len(self.li[0]) == len(next.li)
            ):
                for i, j in zip(dc(self.li), dc(next.li)):
                    row = []
                    for n, m in zip(i, j):
                        row.append(m * n)
                    res.append(row)
        else:
            raise MatrixError(self, next)

        return Matrix(res)

    __rmul__ = __mul__

    def transpose(self):
        res = []
        for i in range(len(self.li[0])):
            row = []
            for j in self.li:
                row.append(j[i])
            res.append(row)
        self.li = res
        return Matrix(self.li)

    def transposed(self):
        res = []
        for i in range(len(self.li[0])):
            row = []
            for j in dc(self.li):
                row.append(j[i])
            res.append(row)
        return Matrix(res)


exec(stdin.read())
