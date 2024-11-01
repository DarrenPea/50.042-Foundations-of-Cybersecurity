# Lab 2: Breaking without Brute Force

- [Lab 2: Breaking without Brute Force](#lab-2-breaking-without-brute-force)
  - [Objectives](#objectives)
  - [Part I: Substitution Cipher](#part-i-substitution-cipher)
    - [Part I's Approach](#part-is-approach)
  - [Part II: Compromising OTP Integrity](#part-ii-compromising-otp-integrity)
    - [Part II's Approach](#part-iis-approach)

## Objectives

* Break a substitution cipher using frequency analysis and write the decryption function in Python
* Encrypt and decrypt using One-Time Pad (OTP)
* Compromise the integrity of a OTP-encrypted message (if knowing the plain text)

## Part I: Substitution Cipher

I am provided with a passage that is encrypted with a substition cipher. I only know a few things about it:

1. It is in "normal" English.
2. Spaces (" ") are preserved (the words are intact).
3. Punctuation may not be preserved.
4. It may consist of any characters included the `string.printable` set
5. I will recognise it when it is decrypted correctly.

The cipher text is provided in this folder (`story_cipher.txt`).

### Part I's Approach

Solution file: `ex1.py`

1. I first decided to create a list of tuples containing each character in `string.printable` and their frequencies in the text and sorted them.
2. Using the frequency analysis of letters of the alphabet in an English corpus, I created a list such that the most frequent letter in the text, "U", is mapped to the most frequent letter in an English corpus, "e", so on.
3. After mapping all the letters, I replaced them and wrote them in `solution.txt`.
4. As expected, not all the letters were replaced correctly in the text, as such, further analysis was required.
5. I looked for words that are more obvious, like "the", "an", "I", etc, and after some replacements, I managed to obtain the original text in `solution.txt`.

Reference: [SAS: The frequency of letters in an English corpus](https://blogs.sas.com/content/iml/2014/09/19/frequency-of-letters.html)

## Part II: Compromising OTP Integrity

In this section, we aim to change an encrypted message **without being able to decrypt it**. 

The aim is to change the **decrypted plain text response** to say I have gotten **4** points, without decrypting it myself. 

In other words, I have to manipulate the **cipher text** , so that it decrypts to a plain text of your choosing.

Thus, the integrity of the encrypted message will be compromised. 

* The ciphertext is encrypted with a OTP, which will be randomly generated. 

### Part II's Approach

Solution file: `ex2.py`

1. Since we know the original text, we can do a `XOR` operation between the original text and the text I wish to input, to obtain a mask.
2. Using the mask, I can do a XOR operation between the original cipher and the mask, which will change the '0' to '4'.
3. After decrypting with the same OTP, the new cipher text will be `Student ID 100XXXX gets 4 points` instead of `Student ID 100XXXX gets 0 points`

Note: The other plaintext will not be affected as the mask for the associated bytes will be 0 since A &oplus; A = 0 in step 1. Then, in step 2, 0 &oplus; B = B so the other portions of the cipher text remains unaffected, except for the bits to change the '0' to '4'.