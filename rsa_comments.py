import random  # Importing the random module to generate random numbers
import math    # Importing the math module for mathematical operations

# Generate two random prime numbers
def generate_primes():
    primes = []  # List to store the generated prime numbers
    while len(primes) < 2:  # Loop until we have generated 2 prime numbers
        prime = random.randint(100, 1000)  # Generate a random number between 100 and 1000
        is_prime = True  # Assume the number is prime initially
        for i in range(2, int(math.sqrt(prime))+1):  # Iterate through possible divisors from 2 to sqrt(prime)
            if prime % i == 0:  # If the number is divisible by any divisor
                is_prime = False  # Then it's not a prime number
                break  # Break out of the loop
        if is_prime:  # If the number passed the primality test
            primes.append(prime)  # Add it to the list of prime numbers
    return primes  # Return the list of generated prime numbers

# Compute the modular inverse of a number
def modinv(a, m):
    for i in range(1, m):  # Iterate through possible values for the inverse
        if (a * i) % m == 1:  # If (a * i) mod m is equal to 1
            return i  # Return the modular inverse
    return None  # If no modular inverse is found, return None

# Generate public and private keys
def generate_keys():
    primes = generate_primes()  # Generate two prime numbers
    p = primes[0]  # Select the first prime number
    q = primes[1]  # Select the second prime number
    n = p * q  # Compute n, the modulus
    phi_n = (p-1) * (q-1)  # Compute Euler's totient function of n
    e = random.randint(1, phi_n)  # Choose a random number e such that 1 < e < phi_n and gcd(e, phi_n) = 1
    while math.gcd(e, phi_n) != 1:  # Ensure e and phi_n are coprime
        e = random.randint(1, phi_n)  # Choose another random number if gcd(e, phi_n) is not 1
    d = modinv(e, phi_n)  # Compute the modular multiplicative inverse of e modulo phi_n
    return ((n, e), (n, d))  # Return the public and private keys as tuples

# Encrypt a message using the public key
def encrypt(message, public_key):
    n, e = public_key  # Unpack the public key tuple
    return pow(message, e, n)  # Compute the ciphertext using modular exponentiation

# Decrypt a message using the private key
def decrypt(ciphertext, private_key):
    n, d = private_key  # Unpack the private key tuple
    return pow(ciphertext, d, n)  # Compute the decrypted message using modular exponentiation

# Test the RSA implementation
public_key, private_key = generate_keys()  # Generate public and private keys
print("Public key:", public_key)  # Print the public key
print("Private key:", private_key)  # Print the private key

message = 243  # Original message to be encrypted
print("Original message:", message)  # Print the original message

ciphertext = encrypt(message, public_key)  # Encrypt the message using the public key
print("Encrypted message:", ciphertext)  # Print the encrypted message

decrypted_message = decrypt(ciphertext, private_key)  # Decrypt the ciphertext using the private key
print("Decrypted message:", decrypted_message)  # Print the decrypted message
