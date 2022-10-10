def abbrev_name(name):
    return f'{name.upper().split()[0][0]}.{name.split()[1][0]}'

print(abbrev_name("Sam Harris"))