from operator import add, sub, mul, floordiv

def word(num):
    def number(func=None):
        return func(num) if func else num
    return number

def actions(operations):
    def f(operand):
        return lambda num: operations(num, operand)
    return f

zero, one, two, three, four, five, six, seven, eight, nine = map(word, range(10))
plus, minus, times, divided_by = map(actions, [add, sub, mul, floordiv])

print(five(times(four())))
