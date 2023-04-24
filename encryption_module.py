from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import csv
import os

def encrypt_password(user, service, key, password):
    # Pad the key to 16 bytes (128 bits) for AES encryption
    key = key.ljust(16, '\x00').encode('utf-8')
    
    # Encode the password strings as bytes
    password_bytes = password.encode('utf-8')

    #padding the password into 16 btyes boundary
    password_bytes = pad(password_bytes, 16)
    
    # Generate a new 16-byte initialization vector (IV)
    iv = AES.new(key, AES.MODE_CBC).iv
    
    #generating a 16-bytes header
    header = get_random_bytes(16)
    
    # Use the key and IV to encrypt the password using AES encryption in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_password = cipher.encrypt(password_bytes)
    
    #checking if the file exist
    file_path = f'data\\user_data\\{user}.csv'
    if os.path.isfile(file_path) == False:
        with open(file_path,mode='w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['service','iv','password'])
        
    with open(file_path, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([service, iv.hex(), encrypted_password.hex()]) 
        
def decrypt(key, iv, encrypted_password):
    
    # converting bacck to bytes
    iv =bytes.fromhex(iv)
    encrypted_password =bytes.fromhex(encrypted_password)
    key =key.ljust(16,'\x00').encode('UTF-8')   
    
    # using key to decrypt the password encrypted in AES encryption in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_password_bytes = cipher.decrypt(encrypted_password)
    decrypted_password = unpad(decrypted_password_bytes, 16).decode('utf-8').replace('\x0e', '')
    
    return decrypted_password
    