import random
import math

# TODO: take input from keyboard
        # save text to file
        # save encrypted text to file
message = "Hello World!"
shift = 3


def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
            # ord() gets the ASCII value
            # add shift and subtract 65 ensure range starting from 0
            # % 26 ensures range of alphabet
            # + 65 return to uppercase ASCII value
            # chr() returns the character
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

encrypted_text = encrypt(message, shift)
decrypted_text = decrypt(encrypted_text, shift)

print(encrypted_text)
print(decrypted_text)