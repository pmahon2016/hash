import rsa

# open public key file and load public key
key_file = open('privkey.key', 'rb')
key_data = key_file.read()
key_file.close()
privkey = rsa.PrivateKey.load_pkcs1(key_data)

file_d = open('message', 'rb')
message = file_d.read()

signature = rsa.sign(message, privkey, 'SHA-256')

print(signature)

key_file = open('publickey.key', 'rb')
key_data = key_file.read()
key_file.close()
pubkey = rsa.PublicKey.load_pkcs1(key_data)
sigver = rsa.verify(message, signature, pubkey)

print(sigver)


