def make_readable(seconds):
    return f'{seconds//3600:02.0f}:{seconds//60%60:02.0f}:{seconds%60:02.0f}'

print(make_readable(60))