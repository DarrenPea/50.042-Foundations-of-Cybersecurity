# Lab 3: MD5, Hashing

- [Lab 3: MD5, Hashing](#lab-3-md5-hashing)
  - [Objectives](#objectives)
  - [Part I: Hashing Using MD5](#part-i-hashing-using-md5)
	- [Part I's Observations](#part-is-observations)
  - [Part II: Break Hashes with Brute Force](#part-ii-break-hashes-with-brute-force)
	- [Part II's Approach](#part-iis-approach)
  - [Part III: Salt](#part-iii-salt)
	- [Part III's Approach](#part-iiis-approach)
	- [Part III's Observations](#part-iiis-observations)
  - [Part IV: Hash Breaking Competition](#part-iv-hash-breaking-competition)
	- [Part IV's Approach](#part-ivs-approach)

## Objectives

* Hashing using MD5
* Crack MD5 hashes using brute-force
* Strengthen MD5 hash using salt and crack the salted hashes again
* Crack more diffucult hashes with available tools

## Part I: Hashing Using MD5

Compute the MD5 hashes for a few random strings and analyse the output.

### Part I's Observations

1. The length of the MD5 hash is always constant, 32 characters, regardless of the length of input string.
2. There are no visible correlations between the hash and input strings. Even if minor changes, like deleting a character, were made, the entire hash completely changed.

Note: There are still possible cryptographic weakness of MD5.
- There is a possibility for MD5 collision attacks, so it is possible for another person to create a file with the same checksum, resulting in a correctupted file.
- There are big MD5 dictionary tables online so it is possible to match some texts with their corresponding hashes.

## Part II: Break Hashes with Brute Force

Hash values were provided in `hash5.txt` and I had to create a script `ex2.py` to reverse the hashes using brute force. I was supposed to hash different input values until I find a hash that matches one in `hash5.txt`.<br>
It is known that the input values have a length of 5 characters.

### Part II's Approach

Solution file: `ex2.py` and `ex2_hash.txt`

1. I first read the MD5 hashes that I was supposed to reverse.
2. Then using `itertools.product`, I generated all possible 5-character strings, where each character could be a letter or a number.
3. After obtaining a string, I hashed it using MD5 and check if it exists within the hashes in step 1.
4. Steps 2 and 3 were repeated until all possible 5-character strings were hashed and compared with the hashes in step 1.

## Part III: Salt

I was required to use the hashes from `ex2_hash.txt` and append a **random** lowercase character as salt to every element in the list. Then, I had to rehash all the passwords using MD5 and store them in `salted6.txt` and the new plaintexts in `plain6.txt`. 

### Part III's Approach

Solution file: `ex3.py` and `ex3_find_plain6.txt`

I used a similar approach as [Part II](#part-iis-approach), but in order to reduce the computation time, I checked if I have already found all 15 plaintexts. If I have found all 15 plaintexts, the function would end.

### Part III's Observations

However, I observed that it still took much longer to crack the salted hash values when compared to the unsalted hash values. This is due to the extra character being introduced, which drastically increased the number of possibilities.

To crack unsalted hashes, attackers can use rainbow tables and match hashes to their plaintexts with the help of readily available online tools like `rockyou.txt`. In comparison, cracking salted hashes would usually involving brute forcing each hash as each hash would be unique even if the plaintext remains the same. As such, a randomly generated salt can help reduce the effectiveness of rainbow tables.

## Part IV: Hash Breaking Competition

A list of hashes was provided in `hashes.txt` and I was required to reverse as many hashes as I could.

### Part IV's approach

Solution file: `ex4.csv` <br>
The first column is the md5 hashes, while the second column is the plaintext that I have cracked.

Firstly, I used `hashcat` in Kali Linux to attempt to crack the hashes using `rockyou.txt` as my wordlist.<br>
However, it only managed to solve a handful of the hashes, so I looked up for other available tools online. Then, I found this [decrypter](https://hashes.com/en/decrypt/hash) online and it managed to decrypt most of the hashes.

In the end, I managed to crack all of the hashes except 2 of them. 