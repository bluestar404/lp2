import random
import math

def generate_primes():
    primes = []
    while len(primes) < 2:
        prime = random.randint(100, 1000)
        is_prime = True
        for i in range(2, int(math.sqrt(prime))+1):
            if prime % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(prime)
    return primes

def modinv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def generate_keys():
    primes = generate_primes()
    p = primes[0]
    q = primes[1]
    n = p * q
    phi_n = (p-1) * (q-1)
    e = random.randint(1, phi_n)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(1, phi_n)
    d = modinv(e, phi_n)
    return ((n, e), (n, d))

def encrypt(message, public_key):
    n, e = public_key
    return pow(message, e, n)

def decrypt(ciphertext, private_key):
    n, d = private_key
    return pow(ciphertext, d, n)

public_key, private_key = generate_keys()
print("Public key:", public_key)
print("Private key:", private_key)

message = 243
print("Original message:", message)

ciphertext = encrypt(message, public_key)
print("Encrypted message:", ciphertext)

decrypted_message = decrypt(ciphertext, private_key)
print("Decrypted message:", decrypted_message)
