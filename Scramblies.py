def scramble(s1, s2):
    s1_dict = {}
    for letter in s1:
        s1_dict[letter] = s1_dict.get(letter, 0) + 1
    is_s1 = True
    for letter in s2:
        if s1_dict.get(letter):
            s1_dict[letter] = s1_dict.get(letter) - 1
            if s1_dict.get(letter) == 0:
                s1_dict.pop(letter)
        else:
            is_s1 = False
            break
    return is_s1

print(scramble('rkqodlw', 'world'))