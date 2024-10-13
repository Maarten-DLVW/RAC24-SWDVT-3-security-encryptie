import random
import string

# create list of characters used to make the key
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

#shuffle the characters to make a key
random.shuffle(key)

# encrypting
def encrypt_message():
    plain_text = input("enter message to encrypt: ")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print(f"encrypted message: {cipher_text}")

# decrypting
def decrypt_message():
    cipher_text = input("enter message to decrypt: ")
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"original message: {plain_text}")

if __name__ == '__main__':
    encrypt_message()
    decrypt_message()