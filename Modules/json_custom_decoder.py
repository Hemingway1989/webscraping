import json

def decode_complex(dict):
    if '__complex__' in dict:
        return complex(dict['real'], dict['imaginary'])
    else:
        return dict

with open('complex_data.json') as file:
    data = file.read()
    z = json.loads(data, object_hook = decode_complex)

print(type(z))
print(z)
    
