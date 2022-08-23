from genericpath import isfile
from importingJSON import data
import json
from PyDictionary import PyDictionary
from pathlib import Path

#forming a cache of dictionary
#if size of file is larger than zero pass
#else write json file

words = list(data)

dict = PyDictionary()
definitions = {}
iteration_count = 0



if Path('dictionary_cache.json').is_file():
    pass
else:
    for i in words[0:]:
        iteration_count+=1
        try:
            definitions[i] = (dict.meaning(i)['Noun'][0:2])
            print(iteration_count)
        except:
            print('FAILED.')

    with open('dictionary_cache.json', 'w', encoding='utf-8') as f:
        json.dump(definitions, f, indent=4, ensure_ascii=False)

