def pig_it(text):
    new_words = []
    for word in text.split():
        new_word = ''
        if len(word) > 1:
            new_word += word[1:] + word[0] + 'ay'
        elif not word.isalpha():
            new_word += word
        else:
            new_word += word + 'ay'
        new_words.append(new_word)
    return ' '.join(new_words)
    

print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay