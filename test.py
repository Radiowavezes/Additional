def reverse(data):
    for index in range(len(data)):
        yield data[index] ** 2, data[index] ** 3

data = [1, 2, 3, 4, 5, 6]
for i in reverse(data):
    print(i)