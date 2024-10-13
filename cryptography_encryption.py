from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
print(key)

# encrypting
plain_text = input("enter message to encrypt: ")
plain_text_bytes = str.encode(plain_text)
cipher_text = f.encrypt(plain_text_bytes)
print(cipher_text)

#decrypting
decrypted_text_bytes = f.decrypt(cipher_text)
decrypted_text = decrypted_text_bytes.decode()
print(decrypted_text)