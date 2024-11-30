import random
import math
import os

# TODO: take input from keyboard
message = "Hello World!"
shift = 3


def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
            # ord() gets the ASCII value
            # subract shift and subtract 65 ensure range starting from 0
            # % 26 ensures range of alphabet
            # + 65 return to uppercase ASCII value
            # chr() returns the character
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
            # same but in range of lowercase
        else:
            result += char

    return result

# get most recent encrypted message
with open('encrypted.txt', 'r') as enc_file:
    lines = enc_file.readlines()
encrypted_text = lines[-1].strip()
enc_file.close

decrypted_text = decrypt(encrypted_text, shift)

# write decrypted message to file
with open('decrypted.txt', 'a') as dec_file:
    dec_file.write(decrypted_text + '\n')
dec_file.close()

print(f"{decrypted_text}\nSaved to decrypted.txt")