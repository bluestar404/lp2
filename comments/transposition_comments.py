import math  # Importing the math module for mathematical operations

key = input("enter key: ")  # Prompting the user to enter a key for encryption

# Encryption
def encryptMessage(msg):
    cipher = ""  # Initializing an empty string to store the encrypted message
    k_indx = 0  # Initializing an index variable for the key
    msg_len = float(len(msg))  # Calculating the length of the message
    msg_lst = list(msg)  # Converting the message string into a list of characters
    key_lst = sorted(list(key))  # Converting the key string into a sorted list of characters

    col = len(key)  # Determining the number of columns based on the length of the key
    row = int(math.ceil(msg_len / col))  # Calculating the number of rows required to accommodate the message
    fill_null = int((row * col) - msg_len)  # Calculating the number of null characters to fill in the matrix
    msg_lst.extend('_' * fill_null)  # Extending the message list with null characters to fill the matrix

    # Creating the matrix by splitting the message list into rows of length equal to the number of columns
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

    # Iterating through each column of the matrix according to the sorted key and concatenating the characters
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])  # Finding the index of the current key character in the sorted key
        cipher += ''.join([row[curr_idx] for row in matrix])  # Concatenating characters from the matrix
        k_indx += 1  # Moving to the next character in the key

    return cipher  # Returning the encrypted ciphertext

# Decryption
def decryptMessage(cipher):
    msg = ""  # Initializing an empty string to store the decrypted message
    k_indx = 0  # Initializing an index variable for the key
    msg_indx = 0  # Initializing an index variable for the message characters
    msg_len = float(len(cipher))  # Calculating the length of the ciphertext
    msg_lst = list(cipher)  # Converting the ciphertext string into a list of characters
    col = len(key)  # Determining the number of columns based on the length of the key
    row = int(math.ceil(msg_len / col))  # Calculating the number of rows required to accommodate the ciphertext
    key_lst = sorted(list(key))  # Converting the key string into a sorted list of characters
    dec_cipher = []  # Initializing an empty list to store the decrypted matrix

    # Creating an empty matrix to store the decrypted characters
    for _ in range(row):
        dec_cipher += [[None] * col]

    # Placing the characters of the ciphertext into the matrix based on the sorted key order
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])  # Finding the index of the current key character in the sorted key

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]  # Placing the current character in the matrix
            msg_indx += 1  # Moving to the next character in the ciphertext

        k_indx += 1  # Moving to the next character in the key

    # Flattening the decrypted matrix into a single string
    msg = ''.join(sum(dec_cipher, []))

    # Removing any trailing null characters from the decrypted message
    null_count = msg.count('_')
    if null_count > 0:
        return msg[: -null_count]

    return msg  # Returning the decrypted plaintext

# Driver Code
msg = input("enter msg : ")  # Prompting the user to enter the message to be encrypted
cipher = encryptMessage(msg)  # Encrypting the message using the encryptMessage function
print("Encrypted Message: {}".format(cipher))  # Printing the encrypted ciphertext
print("Decrypted Message: {}".format(decryptMessage(cipher)))  # Decrypting and printing the original message
