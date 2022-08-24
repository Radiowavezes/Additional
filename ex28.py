n = (input('Please, enter the integer value of seconds: '))
try:    
    m = int(n)
    for i in (range(m, 0, -1)):
      print(i, ', ', sep='', end='')
    print('Go!')
except:
    print("Only integers are allowed")
    