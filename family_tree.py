with open('input.txt') as inf:
    n = inf.readline()
    family = {line.split()[0]: line.split()[1] for line in inf.readlines()}
    
uniq_ppl = set()
for child, parent in family.items():
    uniq_ppl.add(child)
    uniq_ppl.add(parent)
uniq_ppl = sorted(uniq_ppl)

for person in uniq_ppl:
    ind = 0
    person_res = person
    while family.get(person) is not None:
        ind += 1
        person = family.get(person)
    else:
        print(person_res, ind)
