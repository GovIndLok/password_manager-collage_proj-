from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import csv
import os

def encrypt_password(user, service, key, password):
    # Pad the key to 16 bytes (128 bits) for AES encryption
    key = key.ljust(16, '\x00').encode('utf-8')
    
    # Encode the service and password strings as bytes
    service_bytes = service.encode('utf-8')
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
    file_path = f'user_data\\{user}.csv'
    if os.path.isfile(file_path) == False:
        with open(file_path,mode='w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['service','iv','password'])
        
    with open(file_path, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([service,iv.hex(),encrypted_password.hex()])            