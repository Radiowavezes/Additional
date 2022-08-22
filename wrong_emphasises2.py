with open('emphasises_input.txt', 'r', encoding='utf8') as inF:
    vacWords, lines = int(inF.readline()), inF.readlines()
    vac, val, mistakes = set(), set(), 0
for w in range(vacWords):
    elem = lines[w][:-1]
    vac.update(elem.split()), val.update(elem.lower().split())
for word in lines[-1].split():
    if word.lower() in val and word not in vac:
        mistakes += 1
    elif sum(k.isupper() for k in word) != 1:
        mistakes += 1
print(mistakes)
