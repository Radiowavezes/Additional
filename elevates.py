outF = open('output.txt', 'w', encoding='Utf8',)
with open('Elevates_input.txt', encoding='utf-8') as inFile:
    Lst_of_cnddts = [i for i in inFile.readlines()]
dct_of_cnddts = {Lst_of_cnddts.count(i): i for i in Lst_of_cnddts}
ammount = sum(i for i in dct_of_cnddts.keys())
for i in dct_of_cnddts:
    dct_of_cnddts[i] = [dct_of_cnddts.get(i), int(i*100/ammount)]
res_50 = []
res_double = []
for i, j in dct_of_cnddts.items():
    if j[1] > 50.0:
        res_50.append(j[0])
    else:
        res_double.append([j[1], j[0]])
res = sorted(res_double, reverse=True)
if len(res_50) > 0:
    outF.write(*res_50)
else:
    outF.write(res[0][1])
    outF.write(res[1][1])
inFile.close()
outF.close()
