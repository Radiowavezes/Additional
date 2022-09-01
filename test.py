import json


inF =  open('input_for_test.txt', 'r')
outF = open('output_for_test.txt', 'w')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
sheakspire = {}
for word in (inF.read()):
    if word in alphabet:
        sheakspire[word.strip().lower()] = sheakspire.get(word.strip().lower(), 0) + 1
inF.close()
json.dump(sheakspire, outF)
outF.close()

