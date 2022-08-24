with open('input.txt') as inFile:
    __dict = {}
    for line in inFile:
        for i in line.split():
            __dict[i] = __dict.get(i, 0) + 1
for i, j in sorted(list(__dict.items()), key=lambda x: (-x[1], x[0])):
    print(i)
