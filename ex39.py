MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

cond = int(input('''
            If you want to translate the text 
            to morse code, press \'1\'. 
            If you want to translate the text 
            from morse code, press \'2\' and separate 
            letters with spase and words with \'|\''
            '''))

res = []
if int(cond) == 1:
    u_inp = list(input('Please, enter the text: ').upper().split())
    for i in u_inp:
        mo_word = ''
        for j in i:
            mo_word += MORSE_CODE_DICT[j]
            mo_word += ' '
        res.append(mo_word)
else:
    u_inp = list(input('Please, enter the text: ').upper().split('|'))
    my_str = []
    for i in u_inp:
        list_word = []
        my_word = ''
        for j in i:
            if j == ' ':
                list_word.append(my_word)
                my_word = ''
            else:
                my_word += j
        my_str.append(list_word)
    for i in my_str:
        res_word = ''
        for j in i:
            key = get_key(j, MORSE_CODE_DICT)
            if key != None:
                res_word += str(key)
            else:
                res_word += ' '
        res.append(res_word)
print(*res)
