from urllib.parse import quote_plus,unquote_plus




def encode(text):
    encoded = quote_plus(text)
    return encoded


def decode(text):
    decoded = url = unquote_plus(text)
    return decoded