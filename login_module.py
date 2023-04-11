from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import csv

def add_user(user_id, password):
    # Getting 16-byte key for AES encryption
    key = password.encode('utf-8')
    #passkey="USER AUTHENTAICATED"
    # Use the key to encrypt the passkey
    passkey = 'USER AUTHENTICATED'.encode('UTF-8')
    passkey = pad(passkey, 16)
    
    # Generate a random initialization vector (IV)
    iv = get_random_bytes(16)
    
    # Use the key and IV to encrypt the passkey using AES in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_passkey = cipher.encrypt(pad(passkey,16))

    # Save the key, nonce, header, encrypted password, and tag to a CSV file
    with open('data\\user.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_id, cipher.iv.hex(), encrypted_passkey.hex()])


def user_login(user_id, password):
    key =password.ljust(16,'\x00').encode('UTF-8')
    #with open('data\\user.csv',mode='a', newline='') as file:
    with open('data\\user.csv',mode='r',newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == 'test1':
                iv = row[1]
                encrypted_passkey = row[2] 
    
    #converting back to bytes
    iv = bytes.fromhex(iv)
    encrypted_passkey = bytes.fromhex(encrypted_passkey)
    
    cipher =AES.new(key, AES.MODE_CBC, iv)
    passkey = unpad(cipher.decrypt(encrypted_passkey),16).decode('utf-8').replace("\x0e", "")
    if passkey == 'USER AUTHENTICATED':
        return True
    else:
        return False