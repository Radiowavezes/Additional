f = open('bank_input.txt', 'r')
f.readline()
sums = float(f.readline())
f.readline()
fd = [line.strip() for line in f]
fds = list(map(float, fd))


class SetWithSum:
    def __init__(self, s):
        self._items = list(s)
        self._sum = sum(s)

    def add(self, x):
        self._items.append(x)
        self._sum += x
        return self

    def clone(self):
        return SetWithSum(self.items())

    def items(self):
        return self._items

    def sum(self):
        return self._sum

    def __repr__(self):
        return f"<{self._sum},{self._items}>"


def find_sum(s, T, eps):
    s = list(sorted(s))
    L = [SetWithSum([s[0]])]
    n = len(s)
    delta = eps*T/n
    for x in s[1:]:
        U = L
        U.extend([ l.clone().add(x) for l in L])
        U = sorted(U, key=SetWithSum.sum)
        y = U[0]
        L = [y]
        for z in U:
            if (y.sum()+delta) < z.sum() and z.sum() <= T:
                y = z
                L.append(y)
    return max(L, key=SetWithSum.sum)


print(find_sum(fds, sums, eps=0.0001))
