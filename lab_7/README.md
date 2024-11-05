# Lab 7: RSA

- [Lab 7: RSA](#lab-7-rsa)
  - [Objectives](#objectives)
  - [Set-up](#set-up)
  - [Part I: RSA Without Padding](#part-i-rsa-without-padding)
	- [Part I's implementation](#part-is-implementation)
  - [Part II: Protocol Attack](#part-ii-protocol-attack)
    - [Part II's implementation](#part-iis-implementation)
  - [Part III: RSA Digital Signature Protocol Attack](#part-iii-rsa-digital-signature-protocol-attack)
    - [Part III's implementation](#part-iiis-implementation)
  - [Part IV: Defending RSA with Padding](#part-iv-defending-rsa-with-padding)
	- [Part IV's implementation](#part-ivs-implementation)

## Objectives

- Generate keys, encrypt, decrypt, sign and verify using RSA
- Explain the importance of padding in RSA digital signature

## Set-up

Ensure that pycryptodome is installed
	
	pip install pycryptodome --upgrade

Ensure that you can import it using `from Crypto.PublicKey import RSA`

Create your own public key, `mykey.pem.pub` and private key, `mykey.pem.priv` using `RSA.generate`.

## Part I: RSA Without Padding

Create a signature plaintext `message.txt` using the private key, `mykey.pem.priv`. Signatures using RSA is usually applied to the hash of the message. <br>
First, hash the plaintext using SHA-256, then exponentiate the digest. Then, verify the signature using the public key. The resulting exponentiation should be the same as the hash value of the plaintext.

### Part I's implementation

Solution file: `ex2.py`

First, I imported the public and private keys using `Crypto.PublicKey.RSA` to obtain the public key (n, e) and the private key (n, d).

Encryption: <br>
m $\equiv$ x <sup>e</sup> mod n <br>
Decryption: <br>
m $\equiv$ x <sup>d</sup> mod n

To perform large integer exponentiation for encryption and decryption, I used the square and multiply algorithm from `primes.py`. <br>
I proceeded by hashing `message.txt` with `Crypto.Hash.SHA256`, then signing (decrypting) the message. After that, I verified (encrypting) the signature and checked if the final hash is the same value as the initial hash. 

When creating a signature, it is signed using my own private key so using my public key, anyone would be able to verify the signature and ensure that it comes from me.

## Part II: Protocol Attack

RSA has an undesirable property, namely that it is malleable. Attackers can change the ciphertext to another, which leads to a transformation of the plaintext.

RSA Encryption Protocol Attack:
1. Encrypt an integer (e.g. 100) using the public key from the previous part, e.g. y
2. Choose a multiplier s equal to 2 and calculate: y<sub>s</sub> $\equiv$ s <sub>e</sub> mod n
3. Multiply the two numbers: m $\equiv$ y x y <sub>s</sub> mod n
4. Decrypt using the private key from the previous part

### Part II's implementation

Solution file: `ex3.py`

Following the steps above, my original integer was 100 and my multiplier is 2. As a result of the protocol attack, it modified the original integer to 200 instead. 

It is evident that if only an integer is being encrypted and a multiplier is being applied by an attacker, he will be able to transform the integer to his will.

## Part III: RSA Digital Signature Protocol Attack

In this attack, I am supposed to send a message/signature pair, (x, s), to Bob on behalf on Alice, who will use Alice's public key to verify the signature.

#### Alice's part:

1. Take the public key from the previous section as Alice's public key
2. Choose any 1024-bit integer s
3. Compute a new message from s using the public key: x $\equiv$ s <sup>e</sup> mod n
4. On behalf of Alice, send the signature s and the message x to Bob.

#### Bob's part:

1. Using the public key, Bob gets a new digest x': x' $\equiv$ s <sup>e</sup> mod n
2. Bob checks whether x' == x is true
3. If true, s is a valid signature for x and Bob will accept the message/signature pair

### Part III's implementation

Solution file: `ex4.py`

I implemented the above exchange using a much smaller s.

In practise, I believe that if there is no padding, an attacker could possibly manipulate s to their will. Then, verifying s to produce a message that could be malicious or bring about disruptions to the workflow of Bob. Since Bob will also verify s using the same public key, he will accept the message/signature pair and this could lead to severe consequences.

## Part IV: Defending RSA with Padding

I will be using Optimal Asymmetric Encryption Padding (OAEP) for RSA encryption and Probabilistic Signature Standard (PSS) for RSA digital signature to make RSA more secure.

Create an implementation of RSA with basic building functions:

1. `generate_RSA(bits=1024)` which generates the private key and public key in PEM format
2. `encrypt_RSA(public_key_file, message)` which encrypts a string using the public key, stored in the file name `public_key_file`. It will return the ciphertext in base64
3. `decrypt_RSA(private_key_file, cipher)` which decrypts cipher text in base64 using the private key, stored in the file name `private_key_file`. It will return the plaintext
4. `sign_data(private_key_file, data)` which signs the data using the private key. It will return a signature string in base64
5. `verify_sign(public_key_file, sign, data)` which verifies the signature of a given data. It returns either True or False

### Part IV's implementation

I used `RSA.generate()` to generate the private and public keys. For the encryption and decryption process, instead of using my square and multiply algorithm, i used `Crypto.Cipher.PKCS1_OAEP` instead so there will be padding follow OAEP. For the signing and verifying process, I first used SHA-256 to create a digest of the data before using `Crypto.Signature.PKCS1_PSS`.

I tried to redo the protocol attack in Part II with the new RSA but it did not work. With the use of proper padding schemes with RSA, it will add randomness and structure to the plaintext before encryption so the same plaintext will not produce the same ciphertext every time it is encrypted. Ultimately, this prevents the attacker from transforming the ciphertext into another ciphertext, which would change the plaintext as they desire. Hence, the protocol attack will be prevented.