# Lab 4: Block Cipher

- [Lab 4: Block Cipher](#lab-4-block-cipher)
  - [Objectives](#objectives)
  - [PRESENT Block Cipher](#present-block-cipher)
	- [PRESENT's Overview](#presents-overview)
	- [Implementing PRESENT](#implementing-present)
  - [Implementing ECB Mode](#implementing-ecb-mode)
	- [Approach for implementing ECB Mode](#approach-for-implementing-ecb-mode)
  - [Limitations of ECB Mode](#limitations-of-ecb-mode)
	- [Approach to show limitations of ECB Mode](#approach-to-show-limitations-of-ecb-mode)

## Objectives

* Implement the ultra-lightweight PRESENT block cipher
* Understand the limitations of ECB Mode

## PRESENT Block Cipher

### References

- [Publication on PRESENT](https://www.iacr.org/archive/ches2007/47270450/47270450.pdf)

### PRESENT's Overview

- It is a substitution-permutation network that consists of 31 rounds (and 32 keys)
- Each of the 31 rounds consists of XOR to introduce a round key, a non-linear substitution (S-Box) layer and a linear bitwise permutation (pLayer)
- Last (32nd) key is used at the end of the process for post-whitening

#### S-Box

- S-box can be implemented as a fixed lookup table, where every word (4 bits) is substituted based on the lookup table

#### pLayer

- Bits permutation based on values in a fixed table

#### Round Key

- A series of 32 keys is generated from a 80-bit input key
- Every round, a round key will be generated using the 64 leftmost bits
- In each round i:
	- Rotate left 80-bit key by 61 bits
	- Pass 4 bits [79...76] through S-box
	- XOR the bits [19...15] with LSB of round_counter (i)

#### Decryption

- Run PRESENT backwards to decrypt by inverting S-box and pLayer while running the loop in reverse order

### Implementing PRESENT

Solution file: `present.py`

Based on the above overview of the PRESENT cipher and the publication on it, I have implemented PRESENT. It required a lot of bit manipulation, bit shifting and `&` to obtain the values of particular bits.

## Implementing ECB Mode

Encryption has to be performed on `Tux.pbm`. I am also required to extend the code for `present.py` to work for plaintext larger than 64-bits since it only works for 64-bits currently. I was tasked to use Electronic Codebook Mode (ECB) method for this purpose

1. Use ECB mode block cipher to encrypt `Tux.pbm`
2. Decrypt the file and see if the same image can be seen

### Approach for implementing ECB Mode

Solution file: `ecb.py`

Firstly, I created a function that would determine if the plaintext can be split into groups of exactly 64-bits (8 bytes). Else, I would pad it with null bytes. Then, I saved the results into a list, where each element would be 64 bits.

Based on whether encryption (e) or decryption (d) is selected, I would perform the encryption/decryption for PRESENT block cipher accordingly.

To run the file:

`python ecb.py -i [input filename] -o [output filename] -k [key filename] -m [mode]`

## Limitations of ECB Mode

ECB mode reveals some side-channel information about the plaintext pattern in ciphertext.

1. `letter.e` is a secret image encrypted in ECB mode with a secret key
2. I have to recover the plaintext of the original image, which is stored in PBM format. The header information is stored in `header.pbm`, which is known to the attacker
3. The plaintext PBM image is black and white

### Approach to show limitations of ECB Mode

Solution file: `extract.py`

When reading the input file, I skip the header information entirely to only read its contents. Going through each byte of the content, I created a dictionary, which recorded the frequency of bytes that appeared in the input file.

Since the plaintext PBM image is black and white, I replaced the most frequent byte with white, `b'00000000'` and the other byte black, `b'11111111'` and wrote them in the output file after writing the pbm header.

To run the file:

`python extract.py -i letter.e -o op.txt -hh header.pbm`