import rsa
from cryptography.fernet import Fernet

# create the symmetric key
key = Fernet.generate_key()

# write the symmetric key to a file
k = open('symmetric.key','wb')
k.write(key)
k.close()

# create the pub & private keys
(pubkey,privkey)=rsa.newkeys(2048)

# write the public key to a file
pukey = open('publickey.key','wb')
pukey.write(pubkey.save_pkcs1('PEM'))
pukey.close()

# write the private key to a file
prkey = open('privkey.key','wb')
prkey.write(privkey.save_pkcs1('PEM'))
prkey.close()