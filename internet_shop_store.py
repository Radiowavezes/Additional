fin = open('iss_input.txt', 'r', encoding='utf8')
nDict = dict()
for i in fin:
    i = i.split()
    n, g, gNum = i[0], i[1], int(i[2])
    if n not in nDict:
        nDict[n] = {g: gNum}
    else:
        if g not in nDict[n]:
            nDict[n][g] = gNum
        else:
            nDict[n][g] = nDict[n][g] + gNum
fin.close()
for i in sorted(nDict):
    print(i, ':', sep='')
    for j in sorted(nDict[i]):
        print(j, nDict[i][j])