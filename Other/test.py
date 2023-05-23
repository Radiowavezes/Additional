for i in range(1, 1387):
    for j in range(1, 1387):
        if i * 47 + j * 160 == 223728 and i + j == 1387:
            print(i, 'x 47', j, 'x 160')
print('done')