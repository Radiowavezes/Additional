def longest_repetition(chars):
    char_dict = {}
    text = ''
    if not chars:
        return '', 0
    for symbol in chars:
        if symbol in text:
            text += symbol
        else:
            char_dict[len(text)] = char_dict.get(len(text), text)
            text = symbol
    if text:
        char_dict[len(text)] = char_dict.get(len(text), text)
    return char_dict[max(char_dict)][0], max(char_dict)
    
print(longest_repetition(' '))