#/usr/bin/python3

import base64



def encode(text):
    encoded = base64.b64encode(text.encode())
    return encoded.decode()


def decode(text):
    decoded = base64.b64decode(text.encode());
    return decoded.decode()