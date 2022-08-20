nato_dict = {'A': 'Alpha', 
             'B': 'Bravo',
             'C': 'Charlie',
             'D': 'Delta',
             'E': 'Echo',
             'F': 'Foxtrot',
             'G': 'Golf',
             'H': 'Hotel',
             'I': 'India',
             'J': 'Juliett',
             'K': 'Kilo',
             'L': 'Lima',
             'M': 'Mike',
             'N': 'November',
             'O': 'Oscar',
             'P': 'Papa',
             'Q': 'Quebec',
             'R': 'Romeo',
             'S': 'Sierra',
             'T': 'Tango',
             'U': 'Uniform',
             'V': 'Victor',
             'W': 'Whiskey',
             'X': 'X-ray',
             'Y': 'Yankee',
             'Z': 'Zulu'}

def reversed_dict(any_dict):
    reversed_dict = {}
    for i, j in any_dict.items():
        reversed_dict[j.upper()] = i
    return reversed_dict
    
nato_to_aldict = reversed_dict(nato_dict)

cond = int(input('''
             if you want to translate
             the word to Nato dict, press 1.
             To translate words from Nato dict,
             press 2: 
             '''))
if cond == 1:
    word = input('Input the word: ').upper()
    print(*[nato_dict.get(i) for i in word])
else:
    word = (input('Input the words separating them with spaces and commas: ').upper().split(', '))
    print(*[nato_to_aldict.get(i) for i in word if nato_to_aldict.get(i) != None], sep='')
