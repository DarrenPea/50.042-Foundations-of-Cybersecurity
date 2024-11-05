from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import primes

def encrypt(x, n ,e):
    return primes.square_multiply(x, e, n)

def decrypt(x, n, d):
    return primes.square_multiply(x, d, n)

print("Ex 2----------------------------")
# Read the public key (Add your mykey.pem.pub file)
with open('mykey.pem.pub', 'r') as f:
    public_key = f.read()

rsakey = RSA.importKey(public_key)

# Public key
print("public key n:", rsakey.n)
print("public key e:", rsakey.e)

# Read the private key (Add your mykey.pem.priv file)
with open('mykey.pem.priv', 'r') as f:
    private_key = f.read()

rsakey_private = RSA.importKey(private_key)

# Private key
print("private key n:", rsakey_private.n)
print("private key d:", rsakey_private.d)

hash_obj = SHA256.new()
with open('message.txt', 'rb') as f:
    message = f.read()
    hash_obj.update(message)

digest = hash_obj.digest()
print("\ninitial hash:", digest)

digest_int = int.from_bytes(digest, byteorder='big')
s = decrypt(digest_int, rsakey_private.n, rsakey_private.d)

new_message = encrypt(s, rsakey.n, rsakey.e)
byte_length = (new_message.bit_length() + 7) // 8
new_message_bytes = new_message.to_bytes(byte_length, byteorder='big')
print("final hash:", new_message_bytes)

print("\nIs final hash the same as initial hash?", digest == new_message_bytes)