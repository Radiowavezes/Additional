inFile = open('input_for_bo.txt', 'r', encoding='utf8')
bank_accouts = {}
for line in inFile:
    operations = line.split()
    transaction, name = operations[0], operations[1]
    balance = bank_accouts.get(name)
    if transaction == 'DEPOSIT':
        if name in bank_accouts:
            bank_accouts[name] = \
                int(bank_accouts.get(name)) + int(operations[2])
        else:
            bank_accouts[name] = int(operations[2])
    elif transaction == 'WITHDRAW':
        if name in bank_accouts:
            bank_accouts[name] = \
                int(bank_accouts.get(name)) - int(operations[2])
        else:
            bank_accouts[name] = - int(operations[2])
    elif transaction == 'BALANCE':
        if name in bank_accouts:
            print(balance)
        else:
            print('ERROR')
    elif transaction == 'TRANSFER':
        if name in bank_accouts:
            if operations[2] in bank_accouts:
                bank_accouts[operations[2]] = \
                    int(bank_accouts.get(operations[2])) + int(operations[3])
                bank_accouts[name] = \
                    int(bank_accouts.get(name)) - int(operations[3])
            else:
                bank_accouts[operations[2]] = int(operations[3])
                bank_accouts[name] = \
                    int(bank_accouts.get(name)) - int(operations[3])
        else:
            if operations[2] in bank_accouts:
                bank_accouts[name] = - int(operations[3])
                bank_accouts[operations[2]] = \
                    int(bank_accouts.get(operations[2])) + int(operations[3])
            else:
                bank_accouts[name] = - int(operations[3])
                bank_accouts[operations[2]] = int(operations[3])
    elif transaction == 'INCOME':
        for key, value in bank_accouts.items():
            if int(value) > 0:
                bank_accouts[key] = \
                    int(int(value) + int(value) * int(operations[1]) / 100)
