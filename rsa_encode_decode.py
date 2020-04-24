import math
import numpy as np
import random

public_key = 0
private_key = 0

def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(np.ceil(np.sqrt(n))), 2):
        if n % i == 0:
            return False
    return True

def create_keys():
    # generate p
    min = 1000
    max = 50000
    p = random.randint(min, max)
    while (not is_prime(p)):
        p = random.randint(min, max)

    # generate q
    q = random.randint(min, max)
    while (not is_prime(q)):
        q = random.randint(min, max)

    n = p*q
    z = (p - 1)*(q - 1)
    e = random.randint(int(n/10), n)
    while (not math.gcd(e, z)==1):
        e = random.randint(int(n/10), n)

    d = random.randint(int(n/10), n)
    while (not (e*d)%z == 1):
        d = random.randint(int(n/10), n)

    return (n, e), (n, d)

def RSA_encode(str, public_key):
    message = 0
    for char in str:
        message *= 256
        number = int(ord(char))
        message += number
    encrypted = (message ** public_key[1]) % public_key[0]
    return encrypted

def RSA_decode(encrypted, private_key):
    decrypted = (encrypted ** private_key[1]) % private_key[0]


    message = ''
    while decrypted > 0:
        message = chr(decrypted % 256) + message
        decrypted = int(decrypted/256)
    return message

public_key, private_key = create_keys()
print(public_key)
print(private_key)
message = "hello"
encrypted = RSA_encode(message, public_key)
print(encrypted)
message_out = RSA_decode(encrypted, private_key)
print(message_out)
