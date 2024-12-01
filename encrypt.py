message = input("Enter the message to encrypt:\n")
shift = 10


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
            # same but in range of lowercase
        else:
            result += char

    return result

encrypted_text = encrypt(message, shift)

with open('encrypted.txt', 'a') as enc_file:
    enc_file.write(encrypted_text + '\n')
enc_file.close

print(f"{encrypted_text}\nSaved to encrypted.txt")