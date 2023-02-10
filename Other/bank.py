import time

file = open('bank_input.txt', 'r')
file.readline()
tg = (file.readline())
mytable = tg.maketrans(",", ".")
target = float(tg.translate(mytable))
file.readline()
terms = [float(line.strip().translate(mytable)) for line in file]
file.close()


class SetWithSum:
    def __init__(self, terms):
        self._items = list(terms)
        self._sum = sum(terms)

    def add(self, num):
        self._items.append(num)
        self._sum += num
        return self

    def clone(self):
        return SetWithSum(self.items())

    def items(self):
        return self._items

    def sum(self):
        return self._sum

    def __repr__(self):
        return f"<{self._sum},{self._items}>"


def find_sum(terms, target, eps):
    terms = list(sorted(terms))
    result = [SetWithSum([terms[0]])]
    delta = eps * target / len(terms)
    for digit in terms[1:]:
        twin = result
        twin.extend([i.clone().add(digit) for i in result])
        twin = sorted(twin, key=SetWithSum.sum)
        term = twin[0]
        result = [term]
        for num in twin:
            if (term.sum() + delta) < num.sum() and num.sum() <= target:
                term = num
                result.append(term)
    return max(result, key=SetWithSum.sum)

start = time.time()
print(find_sum(terms, target, eps=0))
print(round((time.time() - start) // 60), 'minutes', round((time.time() - start) % 60), 'seconds')
