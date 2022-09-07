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

    def __size__(self):
        return len(self.li), len(self.li[0])


exec(stdin.read())
