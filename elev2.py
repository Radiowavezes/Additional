import math


def my_round(n):
    if n * 100 % 100 > 50:
        return int(n + 1)
    else:
        return int(n)

inF = open('elev_input2.txt', 'r', encoding='utf8')
outF = open('output.txt', 'w', encoding='utf8')
cand_dict = {}
for i in inF:
    j = i.split()
    party = ''.join(j[0:-1])
    voice = ''.join(j[-1])
    cand_dict[party] = int(voice)
inF.close()
ammount = sum(i for i in cand_dict.values())
for i, j in cand_dict.items():
    cand_dict[i] = my_round(j * 450 / ammount)
    print(i, cand_dict[i], file=outF)
outF.close()
