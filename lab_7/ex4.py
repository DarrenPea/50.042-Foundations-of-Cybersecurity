import ex2

print("\n\nEx 4-----------------------------")
print("Alice's part")
print(f"Alice's public key, (n, e): ({ex2.rsakey.n}, {ex2.rsakey.e})")
print("s: 123456789987654321123456789987654321")
s = 123456789987654321123456789987654321
x = ex2.encrypt(s, ex2.rsakey.n, ex2.rsakey.e)
print("x:", x)
print("Sending s and x to Bob")
print("\nBob's part")
digest = ex2.encrypt(s, ex2.rsakey.n, ex2.rsakey.e)
print("x':", digest)
print("x' == x is", digest == x)
if digest == x:
	print("Bob accepts the message/signature pair")
else:
	print("Bob rejects the message/signature pair")