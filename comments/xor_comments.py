# Initialize a string variable with the value 'HelloWorld'
str = 'HelloWorld';

# Convert each character in the string to its ASCII binary representation and concatenate them into one string
result = ''.join(format(ord(x), '08b') for x in str)

# Initialize a string variable with the value '1111111'
val = '1111111';

# Convert the binary strings 'result' and 'val' to integers and perform a bitwise XOR operation between them
y = int(result,2) ^ int(val,2)

# Format the result of the XOR operation as a binary string and print it
print('{0:b}'.format(y))
