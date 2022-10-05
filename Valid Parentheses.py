def valid_parentheses(strng):
    new_strng = ''
    for symbol in strng:
        if symbol in '()':
            new_strng += symbol
    def recursive_parentheses(new_strng):
        if len(new_strng) == 0:
            return True
        else:
            if '()' in new_strng:
                return recursive_parentheses(new_strng.replace('()', ''))
            return False
    return recursive_parentheses(new_strng)


print(valid_parentheses("hi(hi)()"))