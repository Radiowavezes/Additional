# _myDict = {n: n*2 for n in range(5)}
# print(_myDict)
# _myList = [[i, j] for i, j in enumerate(range(1, 10, 2))]
# print(_myList)

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print(f'What is your {q}?  It is {a}.')

# for i in reversed(range(1, 10)):
#     print(i)

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
#     print(f)

# vec = [[1,2,3], [4,5,6], [7,8,9]]
# print(list(i for j in vec for i in j))

# matrix = [
#         [1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
#     ]
# print(list(j[i] for j in matrix for i in range(len(j))))
# transposed = []
# for i in range(len(matrix) + 1):
#     transposed.append([j[i] for j in matrix])
# print(transposed)

# multiples_gen = list(i for i in range(30) if i % 3 == 0)
# print(multiples_gen)

# x = 10
# for i in [1,2,3,4,5]:
#     if i % 2 == 0:
#         break
#     x -= i
# else:
#     x = 10
# print(x)


# sorting by value when value is list of values
# a = {i: j  for i, j in sorted(employees_dict.items(), key=lambda x: x[1][1])}
# b = {i: j  for i, j in sorted(employees_dict.items(), key=lambda x: x[1][0])}

# def print_tree(n): #-> str
#     for i in range(n):
#         for j in range(n - i):
#             print('1', end='')
#         for k in range(2 * i + 1):
#             print('*', end='')
#         print()

# print(print_tree(7))

# import sys

# randomList = ['a', 0, 2]

# for entry in randomList:
#     try:
#         print("The entry is", entry)
#         r = 10/int(entry)
#         break
#     except:
#         print("Oops!", sys.exc_info()[0], "occurred.")
#         print("Next entry.")
#         print()
# print("The reciprocal of", entry, "is", r)

# import sys

# randomList = ['a', 0, 2]

# for entry in randomList:
#     try:
#         print("The entry is", entry)
#         r = 1/int(entry)
#         break
#     except Exception as e:
#         print("Oops!", e.__class__, "occurred.")
#         print("Next entry.")
#         print()
# print("The reciprocal of", entry, "is", r)


# def zero(a=None): return 0 if not a else a(0)
# def one(a=None): return 1 if not a else a(1)
# def two(a=None): return 2 if not a else a(2)
# def three(a=None): return 3 if not a else a(3)
# def four(a=None): return 4 if not a else a(4)
# def five(a=None): return 5 if not a else a(5)
# def six(a=None): return 6 if not a else a(6)
# def seven(a=None): return 7 if not a else a(7)
# def eight(a=None): return 8 if not a else a(8)
# def nine(a=None): return 9 if not a else a(9)
# def plus(y): return lambda x: x + y
# def minus(y): return lambda x: x - y 
# def times(y): return lambda x: x * y
# def divided_by(y): return lambda x: int(x / y)


# print((nine(divided_by(two()))))

# zero=lambda f=None: f(0) if f else 0
# one=lambda f=None:f(1) if f else 1
# two=lambda f=None: f(2) if f else 2
# three=lambda f=None: f(3) if f else 3
# four=lambda f=None: f(4) if f else 4
# five=lambda f=None: f(5) if f else 5
# six=lambda f=None: f(6) if f else 6
# seven=lambda f=None: f(7) if f!=None else 7
# eight=lambda f=None: f(8) if f else 8
# nine=lambda f=None: f(9) if f else 9
# plus=lambda a: lambda b: b+a
# minus=lambda a: lambda b: b-a
# times=lambda a: lambda b: b*a
# divided_by=lambda a: lambda b: b/a

# def plus(y): return lambda x: x+y
# def minus(y): return lambda x: x-y
# def times(y): return lambda x: x*y
# def divided_by(y): return lambda x: x//y

# # Number function generator
# def nf_gen(n):
#      return lambda f=None: n if not f else f(n)

# zero, one, two, three, four, five, six, seven, eight, nine = map(nf_gen, range(10))

# from operator import add, sub, mul, floordiv

# def constant(n):
#     def number(fun=None):
#         return fun(n) if fun else n
#     return number

# def operator(op):
#     def fun(operand):
#         return lambda x: op(x, operand)
#     return fun

# zero, one, two, three, four, five, six, seven, eight, nine = map(constant, range(10))
# plus, minus, times, divided_by = map(operator, [add, sub, mul, floordiv])

# def mix(s1, s2):   
#     a = 'abcdefghijklmnopqrstuvwxyz'
#     result = []
#     for let in a:
#         if s1.count(let) > 1 or s2.count(let) > 1:
#             if s1.count(let) > s2.count(let):
#                 result.append('1:' + s1.count(let)*let)
#             elif s1.count(let) < s2.count(let):
#                 result.append('2:' + s2.count(let)*let)
#             else:
#                 result.append('=:' + s2.count(let)*let)
#     result.sort()
#     result.sort(key=len, reverse=True)
#     return '/'.join(result)
        

# s1 = "my&friend&Paul has heavy hats! &"
# s2 = "my friend John has many many friends &"
# print(mix(s1, s2))

# def rgb_to_hex(r, g, b):
#   return ('{:X}{:X}{:X}').format(r, g, b)

# print(rgb_to_hex(255, 250, 1))

step = 25 % any([2, 3, 5, 7]) == 0
print(step)