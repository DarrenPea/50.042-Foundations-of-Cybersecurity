# Lab 6: Diffie-Hellman Key Exchange

- [Lab 6: Diffie-Hellman Key Exchange](#lab-6-diffie-hellman-key-exchange)
  - [Objectives](#objectives)
  - [Part I: Implementing Square and Multiply](#part-i-implementing-square-and-multiply)
	- [Part I's implementation](#part-is-implementation)
  - [Part II: Diffie-Hellman Key Exchange (DHKE)](#part-ii-diffie-hellman-key-exchange-dhke)
	- [Part II's implementation](#part-iis-implementation)
  - [Notes](#notes)

## Objectives

- Implement Square-Multiply for large integer exponentiation
- Implement Diffie-Hellman Key Exchange

## Part I: Implementing Square and Multiply

The exponentiation of large integers can be efficiently computed using the square and multiply algorithm.

### Part I's implementation

Solution file: `primes.py`

## Part II: Diffie-Hellman Key Exchange (DHKE)

DHKE can be used for key exchange between 2 parties through an insecure channel. I will simulate an exchange of keys using the DHKE protocol, followed by sending an encrypted message.

### Part II's implementation

Solution file: `dhke.py`

#### Set-up

I first set up this key exchange by choosing a large prime p and an integer, a, which is a primitive element or generator in the group. For simplicity, I picked a = 2.

#### Key Generation

I will be creating 2 sets of public and private keys since I am simulating both parties in the key exchange. <br>
I first choose 2 random private keys, b and c, both would be in the range [2, p-2]. Then, I computed the public keys respectively for B and C:
- B = k <sub>pub,B</sub> $\equiv$ a <sup>b</sup> mod p
- C = k <sub>pub,C</sub> $\equiv$ a <sup>c</sup> mod p

#### Computing Shared Key

I will then exchange the public keys and compute the shared keys:
- k <sub>BC</sub> $\equiv$ C <sup>b</sup> mod p
- k <sub>BC</sub> = k $\equiv$ B <sup>c</sup> mod p

#### Message

I created a random message and encrypted it using the shared key and PRESENT, which was implemented in `lab_4`. After receiving the encrypted message, I ensured that the other party could decrypt the message using the shared key.

## Notes

1. How could we perform the exchange of keys in the real world? Do we need a secure channel? Why or why not?

	The exchange of keys can be done using a reliable channel like TCP, involving a TCP handshake. Then, there will be a TLS handshake between both parties. For example, if DHKE is used, A sends his public key and signs it with his private key, which allows B to verify if the public key came from A. After verifying, B generates a public key and sends it to A, and now both have the same shared key. DHKE does not require a secure channel. It can be performed over an authenticated channel as the shared parameters, p and alpha, can be known to public. It will be impossible to obtain the shared key as one would require the private key to compute the shared key. Hence, oly an authenticated channel would be needed to prevent the public key from being tampered with.

2. What is an advantage and a disadvantage of DHKE?

	An advantage of DHKE is that it allows a secure key exchange over an insecure channel. Using a public and a private key, it creates a shared key for both parties and provides secure communication between both. <br>
	A disadvantage of DHKE is that it is vulnerable to man-in-the-middle (MITM) attacks as there is a lack of proper authentication. An attacker can intercept and replace the public keys, resulting in both parties establishing a shared key with the attacker instead of one another.