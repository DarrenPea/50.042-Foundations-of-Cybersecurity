import ex2
import primes

print("\n\nEx 3-----------------------------")
number = 100
print("Encrypting:", number)
print("Result:")
y = ex2.encrypt(number, ex2.rsakey.n, ex2.rsakey.e)
print(y)
s = 2
y_s = primes.square_multiply(s, ex2.rsakey.e, ex2.rsakey.n)

print("Modified to:")
m = (y * y_s) % ex2.rsakey.n
print(m)
message = ex2.decrypt(m, ex2.rsakey_private.n, ex2.rsakey_private.d)
print("Decrypted:", message)