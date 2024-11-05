from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode
from Crypto.Util.number import bytes_to_long, long_to_bytes

def generate_RSA(bits=1024):
	mykey = RSA.generate(bits)
	private_key = mykey.exportKey('PEM')
	public_key = mykey.publickey().exportKey('PEM')
	with open('public_key_file.pem', 'wb') as f:
		f.write(public_key)
	with open('private_key_file.pem', 'wb') as f:
		f.write(private_key)

def encrypt_RSA(public_key_file, message):
	with open(public_key_file, 'rb') as f:
		public_key = f.read()
	rsa_public_key = RSA.importKey(public_key)
	rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
	encrypted = rsa_public_key.encrypt(message.encode())
	return b64encode(encrypted).decode()

def decrypt_RSA(private_key_file, encrypted_message):
	with open(private_key_file, 'rb') as f:
		private_key = f.read()
	rsa_private_key = RSA.importKey(private_key)
	rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
	decrypted = rsa_private_key.decrypt(b64decode(encrypted_message))
	return decrypted.decode()

def sign_data(private_key_file, data):
	with open(private_key_file, 'rb') as f:
		private_key = f.read()
	rsa_private_key = RSA.importKey(private_key)
	hash = SHA256.new(data.encode())
	signer = PKCS1_PSS.new(rsa_private_key)
	signature = signer.sign(hash)
	return b64encode(signature).decode()

def verify_sign(public_key_file, sign, data):
	with open(public_key_file, 'rb') as f:
		public_key = f.read()
	rsa_public_key = RSA.importKey(public_key)
	hash = SHA256.new(data.encode())
	verifier = PKCS1_PSS.new(rsa_public_key)
	try:
		verifier.verify(hash, b64decode(sign))
		return True
	except:
		return False


if __name__ == '__main__':
	print("\n\nEx 5-----------------------------")

	generate_RSA()
	with open('mydata.txt', 'r') as f:
		data = f.read()
	encrypted_mydata = encrypt_RSA('public_key_file.pem', data)
	print("Encrypted data:", encrypted_mydata)
	decrypted_mydata = decrypt_RSA('private_key_file.pem', encrypted_mydata)
	print("\nDecrypted data:", decrypted_mydata)
	signed = sign_data('private_key_file.pem', data)
	print("Verification if signature is valid:", verify_sign('public_key_file.pem', signed, data))


	print("\n\nProtocol Attack\n")
	print("Encrypting: 100")
	message = 100
	encrypted_test = encrypt_RSA('public_key_file.pem', str(message))
	print("Result:", encrypted_test)

	encrypted_test_bytes = b64decode(encrypted_test)
	y = bytes_to_long(encrypted_test_bytes)
	
	s = 2
	encrypted_s = encrypt_RSA('public_key_file.pem', str(s))
	encrypted_s_bytes = b64decode(encrypted_s)
	y_s = bytes_to_long(encrypted_s_bytes)

	with open('public_key_file.pem', 'rb') as f:
		public_key = RSA.import_key(f.read())

	m = (y * y_s) % public_key.n
	modified_encrypted = b64encode(long_to_bytes(m)).decode()
	print("Modified to:", modified_encrypted)
	print('\n')
	try:
		decrypted_test = decrypt_RSA('private_key_file.pem', modified_encrypted)
		print("Decrypted:", decrypted_test)
	except (ValueError):
		print("The attack fails because the decrypted message is not the same as the original message")