def expanded_form(n):
    # grade = 10**(len(str(n))-1)
    # trunc = 10
    # remainder = 1
    # expanded = []
    # while trunc <= grade:
    #     figure = n % trunc // remainder * remainder
    #     if figure:
    #         expanded.append(n % trunc // remainder * remainder)
    #     trunc *= 10
    #     remainder *= 10
    # expanded.append(n // remainder * remainder)
    # return ' + '.join(str(figure) for figure in expanded[::-1])
    a = sorted(enumerate(str(n)[::-1]), reverse=True)
    return ' + '.join(y + '0' * x for x, y in a if y != '0')

print(expanded_form(52004))
