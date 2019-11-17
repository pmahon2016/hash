import rsa


def create_file(file):
    key_file = open(file, 'wb')
    return key_file


# create the pub & private keys
(pubkey, privkey) = rsa.newkeys(2048)

# write the public key to a file
create_file('publickey.key').write(pubkey.save_pkcs1('PEM'))

# write the private key to a file
create_file('privatekey.key').write(privkey.save_pkcs1('PEM'))


