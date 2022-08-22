inFile = open('emphasises_input.txt', 'r', encoding='utf8')
emphas_dict = []
user_dict = []
n = int(inFile.readline())
for line in range(n):
    emphas_dict.append(inFile.readline().strip())
for word in inFile.readline().split():
    user_dict.append(word)
inFile.close()
emphas_dict_lower = [word.lower() for word in emphas_dict]
mistakes = 0
for user_word in zip(user_dict):
    if (user_word.lower()) in emphas_dict_lower:
        if user_word not in emphas_dict:
            mistakes += 1
    else:
        is_upper = 0
        for letter in user_word:
            if letter.isupper():
                is_upper += 1
        if is_upper > 1 or is_upper == 0:
                mistakes += 1
print(mistakes)
