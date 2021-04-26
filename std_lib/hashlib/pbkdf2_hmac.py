import hashlib

with open('./pbkdf2_passwd') as f:
    contents = f.readlines()

hash_name = 'sha256'
salt = bytearray(contents[0], 'utf-8')
password = contents[1].encode('utf-8')
iterations = 100000

pass_hash = hashlib.pbkdf2_hmac(hash_name, password, salt, iterations)
print(pass_hash)
f = open('.hthash', 'wb')
f.write(pass_hash)
f.close()
