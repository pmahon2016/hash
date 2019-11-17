# This file signs a file with the owner's private key and
# verifies the signature with the owners public key
import rsa


# Open key file and return key data
def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data


# Open private key file and load in key
privkey = rsa.PrivateKey.load_pkcs1(file_open('privkey.key'))

# Open the secret message file and return data to variable
message = file_open('message')

# Sign the message with the owners private key
signature = rsa.sign(message, privkey, 'SHA-256')

print(signature)

# change the message to show verification

# Open public key file and load in key
pubkey = rsa.PublicKey.load_pkcs1(file_open('publickey.key'))

# Verify the signature to show if successful or failed
try:
    rsa.verify(message, signature, pubkey)
    print("Signature successfully verified")

except:
    print("Warning!!!! Signature could not be verified")
