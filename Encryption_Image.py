from Crypto.Cipher import DES3
from hashlib import md5

file_path = "sample.jpg"
key = "hello"

key_hash = md5(key.encode('ascii')).digest()
tdes_key = DES3.adjust_key_parity(key_hash)
cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')

with open(file_path, 'rb') as input_file:
    file_bytes = input_file.read()
    new_file_bytes = cipher.encrypt(file_bytes)

with open(file_path, 'wb') as output_file:
    output_file.write(new_file_bytes)
    print("Done!!!")
