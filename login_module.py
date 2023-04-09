from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import csv

def add_user(user_id, password):
    # Generate a new 16-byte key for AES encryption
    key = password.encode('utf-8')
    #passkey="USER AUTHENTAICATED"
    # Use the key to encrypt the user's password
    passkey = 'USER AUTHENTICATED'.encode('UTF-8')
    passkey = pad(passkey, 16)
    
    # Generate a random initialization vector (IV)
    iv = get_random_bytes(16)
    
    # Use the key and IV to encrypt the passkey using AES in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_passkey = cipher.encrypt(passkey)

    # Save the key, nonce, header, encrypted password, and tag to a CSV file
    with open('data\\user.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_id, cipher.iv.hex(), encrypted_passkey.hex()])
