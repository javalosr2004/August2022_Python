import json

f = open('words_dictionary.json') #opens the file
dictionary = json.load(f)



dictionary = set(dictionary.items())


print(dictionary.pop()[0])