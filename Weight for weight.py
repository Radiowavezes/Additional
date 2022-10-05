def order_weight(strng):
    def sorting_sum(x):
        res = 0
        for symb in str(x):
            res += int(symb)
        return res
    new_strng = list(enumerate(map(int, strng.split())))
    new_strng = sorted(new_strng, key = lambda x: sorting_sum(x[1]), reverse=True)
    return ' '.join(str(i[1]) for i in new_strng[::-1])


strng = "2000 10003 1234000 44444444 9999 11 11 22 123"
print(order_weight(strng))