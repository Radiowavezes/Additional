infile = open('input.txt', 'r', encoding='utf-8')
persons = {}
for line in infile:
    temp = line.split()
    person, good, volume = temp[0], temp[1], int(temp[2])
    if person in persons:
        if good in persons[person]:
            persons[person][good] += volume
        else:
            persons[person][good] = volume
    else:
        persons[person] = {good: volume}
infile.close()
for person in sorted(persons):
    print(person, ':', sep="")
    for good in sorted(persons[person]):
        print(good, persons[person][good])
