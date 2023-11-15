
a, b, c = 'x', None, []

print(not a if a or b else c)

import json

data = {
    "Name":"saqib"
}

result = json.dumps(data)

print(type(result))


idctttt = {
    "tags": ['saqib', 'aaqib'],
}


print(idctttt.get('tag', []))

a = ['1', '2', '3', '4', '5']
print(len(a))