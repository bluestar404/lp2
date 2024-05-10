# The Crypto package provides cryptographic algorithms and protocols for secure communications.
# Within the Crypto package, the Cipher module allows encryption and decryption operations using various encryption algorithms.
from Crypto.Cipher import DES

key = b'adityaba'  # Define encryption key

# Create a new DES cipher object with ECB (Electronic Codebook) mode
# ECB mode encrypts each block of plaintext independently, which can lead to patterns in the ciphertext if the same plaintext blocks repeat.
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b'This is a secret'  # Define the plaintext to be encrypted

# Calculate padding length required for DES encryption
# DES operates on 64-bit blocks, so the plaintext needs to be padded to a multiple of 8 bytes.
padding_length = 8 - (len(plaintext) % 8)

# Pad plaintext according to DES block size
plaintext += bytes([padding_length]) * padding_length

# Encrypt the padded plaintext using DES cipher
ciphertext = cipher.encrypt(plaintext)

# Decrypt the ciphertext using DES cipher
decrypted_plaintext = cipher.decrypt(ciphertext)

# Extract padding length from decrypted plaintext
padding_length = decrypted_plaintext[-1]

# Remove padding from decrypted plaintext
decrypted_plaintext = decrypted_plaintext[:-padding_length]

# Print the original plaintext
print("Original text:", plaintext)

# Print the encrypted ciphertext
print("Encrypted text:", ciphertext)

# Print the decrypted plaintext
print("Decrypted text:", decrypted_plaintext)
