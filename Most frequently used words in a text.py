from curses.ascii import isalpha


def top_3_words(text):
    words = (' '.join(text.split('\n'))).split()
    new_words = []
    for word in words:
        new_word = ''
        for letter in word:
            if letter.isalpha() or letter == '\'':
                new_word += letter.lower()
        for letter in new_word:
            if letter.isalpha():
                new_words.append(new_word)
                break
    words_dict = {}
    for word in new_words:
        words_dict[word] = words_dict.get(word, 0) + 1
    result = sorted(words_dict, key=lambda x: words_dict.get(x), reverse=True)
    return result[:3]

text = '  , e   .. '

print(top_3_words(text))