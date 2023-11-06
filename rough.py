
a, b, c = 'x', None, []

print(not a if a or b else c)

import json

data = {
    "Name":"saqib"
}

result = json.dumps(data)

print(type(result))
