import string
from math import gcd as bltin_gcd

M = 26

def coprime(a, b):
    return bltin_gcd(a, b) == 1


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError
    else:
        return x % m

# E(x) = (ax + b) mod m
def encode(plain_text, a, b):
    if not coprime(a, M):
        raise ValueError
    encoded_string = []
    plain_text = plain_text.strip()
    plain_text = plain_text.lower()
    plain_text = plain_text.replace(".", "")
    plain_text = plain_text.replace(",", "")
    plain_text = plain_text.replace(" ", "")
    space = 0
    for i in plain_text:
        if space == 5:
            encoded_string.append(" ")
            space = 0
        if i.isdigit():
            encoded_string.append(i)
        else:
            x = string.ascii_lowercase.index(i)
            encoded_position = ((a * x) + b) % M
            encoded_string.append(string.ascii_letters[encoded_position])
        space += 1
    return "".join(encoded_string)

# D(y) = a^-1(y - b) mod m
def decode(ciphered_text, a, b):
    ciphered_text = ciphered_text.replace(" ", "")
    plain_text = []
    for i in ciphered_text:
        if i.isdigit():
            plain_text.append(i)
        else:
            y = string.ascii_letters.index(i)
            plain_position = modinv(a % M, M) * (y - b) % M
            plain_text.append(string.ascii_letters[plain_position])
    return "".join(plain_text)
