def increment_string(strng):
    num_strng = ''
    let_strng = ''
    if strng[-1].isdigit() == False or len(strng) == 0:
        strng += '1'
    else:
        for i in strng[::-1]:
            if i.isdigit():
                num_strng += i
            else:
                let_strng += i
    number = int(num_strng[::-1])
    if number > 100:
        strng = let_strng[::-1] + '100'
    else:
        strng = let_strng[::-1] + str(number + 1)
    return strng    


print(increment_string("foobar099"))