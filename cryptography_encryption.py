from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

# encrypting
def encrypt_text():
    plain_text = input("enter message to encrypt: ")
    plain_text_bytes = str.encode(plain_text)
    cipher_text = f.encrypt(plain_text_bytes)
    print(f"encrypted message: {cipher_text}")

#decrypting
def decrypt_text():
    encrypted_text_input = input("enter encrypted message to decrypt: ")
    decrypted_text_bytes = f.decrypt(encrypted_text_input)
    decrypted_text = decrypted_text_bytes.decode()
    print(f"decrypted message: {decrypted_text}")
    
if __name__ == '__main__':
    encrypt_text()
    decrypt_text()