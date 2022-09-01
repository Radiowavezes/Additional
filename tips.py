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

print(sum(range(1, 5)))
