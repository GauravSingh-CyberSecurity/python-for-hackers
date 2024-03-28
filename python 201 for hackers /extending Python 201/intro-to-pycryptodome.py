# https://www.pycryptodome.org/
# https://pypi.org/project/pycryptodome/\

# pip install pycryptodome       

#lets use AES cipher (symmetric encription)

from Crypto.Random import get_random_bytes

print("\n----------------------------------------------------")

key = get_random_bytes(32)  #this key is 32 bytes i.e 256 bits & this key is completly random and generated a new one at each execution of the file
print("random symmertic key without salt :- \n {}".format(key))
print("\n length of the symmetric key is = {}" .format(len(key)))

print("\n----------------------------------------------------")




#to generate PW based symmetric key i.e using a PW to make the key
from Crypto.Protocol.KDF import PBKDF2

#Random salt
salt = get_random_bytes(32)
password = "hunter2"
key = PBKDF2(password,salt,dkLen=32)
print("generated at every execution of the py code a random symmertic key and with a random salt  :- \n {}".format(key))
print("\n length of the salted symmetric key is = {}" .format(len(key)))

print("\n----------------------------------------------------")


# using a Static value for salting 
salt =  b")e\xb1\xa6\xb8jP@'\xeb \xf6_R\x04\xa5=\xd5\xedb\x90\x1c\x85\xde7\x9c\xde\xd7D\xc1\xd5\xee"
password = "hunter2"                            #static salted key will be fixed for every password
password2 = "hunter1"
key = PBKDF2(password,salt,dkLen=32)
key2 = PBKDF2(password2,salt,dkLen=32)


#generated at every execution of the py code a random symmertic key and with a static salt i.e this string of key will always be the same as it is converted to  static salt value after a random key is generated 
print(" static salted key with PW({}) :- \n {}".format(password,key))
print("\n length of the salted symmetric key is = {}" .format(len(key)))                         ,  print("\n")

print("static salted key with PW({}) :- \n {}".format(password2,key2))
print("\n length of the salted symmetric key is = {}" .format(len(key2)))



'''Salting : Salt in cryptography is a random value added to data before it is hashed to ensure that even if the same data is hashed multiple times, the resulting
hashes will be different. This helps protect against attacks like rainbow table attacks, where precomputed hashes are used to quickly crack passwords. Salt adds 
uniqueness to each hash, making it more secure.

static salt = fixed key value
dynamic salt= random key value generated every time this code is run/executed
'''









print("\n----------------------------------------------------")


# After understanding & generating keys now lets go to symmetric block cipher i.e AES encryption 

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad , unpad

to_encrypt = b"encrypt me!"

cipher = AES.new(key, AES.MODE_CBC)
print("Initialization vector :- \n {}".format(cipher.iv))                   ,print("\n")
cipher_data = cipher.encrypt(pad(to_encrypt, AES.block_size))
print("Cipher text (Encrypted data):- \n {}".format(cipher_data))


print("\n")


cipher = AES.new(key, AES.MODE_CBC, iv=cipher.iv)
plain_text_data = unpad(cipher.decrypt(cipher_data),AES.block_size )
print("Plain text :- \n {}".format(plain_text_data))





print("\n----------------------------------------------------")

# Now symmetric stream cipher  i.e ARC4 (Alleged RC4), also known as ARCFOUR

from Crypto.Cipher import ARC4
cipher = ARC4.new(key)
encrypted = cipher.encrypt(to_encrypt)
print("cipher text using stream cipher:- \n {}".format(encrypted))

print("\n")

cipher = ARC4.new(key)
plain_text = cipher.decrypt(encrypted)
print("plain text using stream cipher:- \n {}".format(plain_text)) 





print("\n----------------------------------------------------")

# Now Asymmetric key cryptography i.e RSA

from Crypto.PublicKey import RSA

key = RSA.generate(1024)  #bits

encrypted_private_key = key.exportKey(passphrase=password)
print(encrypted_private_key) #prints encrypted RSA private key

print("\n")

public_key = key.publickey()
print(public_key.exportKey()) #prints RSA public key i.e also not encrypted  

print("\n")

print(key.can_encrypt())
print(key.can_sign())
print(key.has_private())
print(public_key.has_private())



print("\n----------------------------------------------------")
'''PKCS1_OAEP is a cipher for RSA encryption and decryption using the Optimal Asymmetric Encryption Padding (OAEP) scheme defined in PKCS#1 v2.1. OAEP provides a more secure padding scheme compared to the older PKCS#1 v1.5 padding. It helps protect against certain cryptographic attacks, particularly those related to padding oracle vulnerabilities.

Here's a brief overview of the key points about PKCS1_OAEP encryption:

Padding Scheme: OAEP is a padding scheme used with RSA encryption to ensure the security of the message being encrypted. It adds randomness to the plaintext before encryption, making it more resistant to certain attacks.

Security: OAEP is designed to be provably secure against chosen-plaintext attacks, assuming RSA is secure. It offers a higher level of security compared to the older PKCS#1 v1.5 padding.

Usage: PKCS1_OAEP is commonly used in applications where RSA encryption is needed, such as secure messaging, digital signatures, and key exchange protocols like TLS.

Cryptographic Operations:

Encryption: Encrypts the plaintext using the RSA public key and OAEP padding.
Decryption: Decrypts the ciphertext using the RSA private key and verifies the OAEP padding.
Implementation: In Python's Crypto.Cipher module, PKCS1_OAEP is implemented as a cipher object that can be used for encryption and decryption operations with RSA keys.

Overall, PKCS1_OAEP provides a secure and efficient way to encrypt and decrypt messages using RSA encryption.'''



from Crypto.Cipher import PKCS1_OAEP

#to_encrypt = b"A" *1000         #we cant use a very long P.T in RSA OAEP(ValueError: Plaintext is too long.)

cipher = PKCS1_OAEP.new(public_key)
encrypted = cipher.encrypt(to_encrypt)
print("C.T using RSA OAEP :- \n {}".format(encrypted))                 ,print("\n")

cipher = PKCS1_OAEP.new(key)
plain_text = cipher.decrypt(encrypted)
print("P.T using RSA OAEP :- \n {}".format(plain_text))




print("\n----------------------------------------------------")


#Digital signature (SHA (Secure Hash Algorithm) is a cryptographic hash function, which means it is used to generate a fixed-size hash value (digest) from input data of arbitrary size. So, SHA is a hash function, and the output it produces is called a hash or message digest.)

from Crypto.Hash import SHA512

plain_hash = SHA512.new(to_encrypt).digest()
hashed = int.from_bytes(plain_hash, byteorder='big')
print("P.T Hash : {}".format(hashed))                                           ,print("\n")

signature = pow(hashed, key.d, key.n)
print("Signature : {}".format(signature))               ,print("\n")

signature_hash = pow(signature, key.e, key.n)
print("signature hash : {}".format(signature_hash))


print("\n",hashed == signature_hash)