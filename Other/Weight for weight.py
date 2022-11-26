def order_weight(strng):
    def sorting_sum(x):
        res = 0
        for symb in str(x):
            res += int(symb)
        return res
    new_strng = sorted(strng.split(), key = lambda x: sorting_sum(x))
    return ' '.join(str(i) for i in new_strng)


strng = "2000 10003 1234000 44444444 9999 11 11 22 123"
print(order_weight(strng))