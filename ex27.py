username, password = input('Username: '), input('Password: ')
for i in reversed(range(3)):
    username_input = input('Please, input your username: ')
    if username_input == username:
        res_user = 'Ok'
        print(res_user)
        break
    else:
        print('There\'s no user with such username. Please, try again. You have %i attempts left' %(i))
        res_user = 'False'
if res_user == 'Ok':
    for i in reversed(range(3)):
        password_input = input('Please, enter your password: ')
        if password_input == password:
            print('You\'ve logged in!!!')
            res_pas = 'Ok'
            break
        else:
            print('Wrong password. Please, try again. You have %i attempts left' %(i))
            res_pas = 'False'
    if res_pas != 'Ok':
        print('You\'ve blocked')
else:
    print('You have no more attempts. Please, try again later')
