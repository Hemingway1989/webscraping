import json

class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            super().default(self, z)
            type_name = z.__class__.__name__
            raise TypeError(f"Object of type {type_name} is not JSON serializable")

json_str = json.dumps(4+6j, cls = ComplexEncoder)
print(json_str)
