final_cost = 0
result_list = []
while True:
    while True:
        n = input('Are you a member or not? Type \'y/n\': ')
        if n == 'n':
            final_cost += 3
            break
        elif n == 'y':
            final_cost += 1.5
            break
        else:
            print('Please, type y/n whether you are a member or not. ')

    while True:
        m = input('How many hours have you parked: ')
        try:
            hours = int(m)
            break
        except:
            print('Invalid entry. Must an integer: ')
            
    if hours == 1:
        final_cost += 2
    elif hours == 2:
        final_cost += 3.5
    elif hours == 3:
        final_cost += 4.5
    else:
        hours -= 3
        final_cost += 4.5 + hours * 0.5
        
    print('Total amount is %d$' % final_cost)
    result_list.append(final_cost)
    final_cost = 0
    
    while True:
        k = input('Do you want to input another driver? y/n: ')
        if k == 'y' or k == 'n':
            break
        else:
            print('Please, enter y/n if you want to input another driver: ')
            
    if k == 'n':
        print(f'{len(result_list)} Driver payed. The total earnings are {sum(result_list)}$')
        break
    elif k == 'y':
        continue
