import json

# dump()
# write data to a file-like object in JSON format

data = {
    'user': {
        'name': 'Johnny Johnsson',
        'age': 36
    }
}

with open('json_file.json', 'w') as write_file:
    json.dump(data, write_file, indent = 4)

# dumps()
# Write data to a string in JSON format

json_str = json.dumps(data, indent = 4)
print(json_str)
