from Crypto.Cipher import AES  # Import AES encryption module
from Crypto.Random import get_random_bytes  # Import random byte generator

key = get_random_bytes(16)  # Generate a random 128-bit (16 bytes) key for AES

# Create a new AES cipher object with ECB (Electronic Codebook) mode
# ECB mode encrypts each block of plaintext independently, which can lead to patterns in the ciphertext if the same plaintext blocks repeat.
cipher = AES.new(key, AES.MODE_ECB)

plaintext = b'This is a secret'  # Define the plaintext to be encrypted

# Calculate padding length required for AES encryption
# AES operates on 128-bit (16 bytes) blocks, so the plaintext needs to be padded to a multiple of 16 bytes.
padding_length = 16 - (len(plaintext) % 16)

# Pad plaintext according to AES block size
plaintext += bytes([padding_length]) * padding_length

# Encrypt the padded plaintext using AES cipher
ciphertext = cipher.encrypt(plaintext)

# Decrypt the ciphertext using AES cipher
# Note: For decryption, you need to create a new AES cipher object with the same key and mode.
decipher = AES.new(key, AES.MODE_ECB)
decrypted_plaintext = decipher.decrypt(ciphertext)

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
