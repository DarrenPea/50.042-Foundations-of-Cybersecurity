import itertools
import string
import time
import hashlib

answers = []
with open("hash5.txt") as f:
	text = f.readlines()
	for i in range(len(text)):
		text[i] = text[i].replace("\n", "")
	
	start_time = time.time()

	characters = string.ascii_lowercase + string.digits
	for attempt in itertools.product(characters, repeat=5):
		attempt = "".join(attempt)
		result = hashlib.md5(attempt.encode()).hexdigest()
		if result in text:
			answers.append(attempt)
	
	execution_time = time.time() - start_time
	print(execution_time)

with open("ex2_hash.txt", "w") as ans:
	ans.write("\n".join(answers))