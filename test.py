def to_camel_case(text):
    for symb in '_-':
        while symb in text:
            text = text.replace(symb, ' ')
    new_text1 = text.split()
    new_text2 = list(word.capitalize() for word in new_text1[1:])
    return new_text1[0] + ''.join(new_text2)

print(to_camel_case('the_stealth_warrior'))
print(to_camel_case("The-Stealth-Warrior"))