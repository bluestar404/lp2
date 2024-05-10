from Crypto.Cipher import DES

key = b'adityaba'

cipher = DES.new(key,DES.MODE_ECB)

plaintext = b'This is a secret'

padding_length = 8 - (len(plaintext) % 8)
plaintext += bytes([padding_length]) * padding_length

ciphertext = cipher.encrypt(plaintext)

decrypted_plaintext = cipher.decrypt(ciphertext)

padding_length = decrypted_plaintext[-1]
decrypted_plaintext = decrypted_plaintext[:-padding_length]

print("Original text:", plaintext)
print("Encrypted text:", ciphertext)
print("Decrypted text:", decrypted_plaintext)