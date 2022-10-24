def make_readable(seconds):
    return f'{seconds//3600:02.0f}:{seconds//60%60:02.0f}:{seconds%60:02.0f}'

def make_readable2(s):
    return '{:02}:{:02}:{:02}'.format(s // 3600, s // 60 % 60, s % 60)

print(make_readable(60))
print(make_readable2(60))