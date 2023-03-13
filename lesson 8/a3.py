import json

with open("my.json", 'r') as my_json:
    a = json.load(my_json)
    print(*a['names'], sep='\n')

with open("my.json", 'w') as my_json:
    a['names'].append('Damir')
    json.dump(a, my_json)