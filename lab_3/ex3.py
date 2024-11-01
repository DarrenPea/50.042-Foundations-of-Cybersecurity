import itertools
import string
import time
import hashlib
import random

new_hashes = []
with open("ex2_hash.txt") as old_f:
	old_text = old_f.readlines()
	salt = random.choice(string.ascii_lowercase)
	for i in range(len(old_text)):
		old_text[i] = old_text[i].replace("\n", "") + salt
	for new_pass in old_text:
		result = hashlib.md5(new_pass.encode()).hexdigest()
		new_hashes.append(result)

with open("salted6.txt", "w") as salted6:
	salted6.write("\n".join(new_hashes))

with open("plain6.txt", "w") as plain6:
	plain6.write("\n".join(old_text))


answers = []

with open("salted6.txt") as f:
	text = f.readlines()
	for i in range(len(text)):
		text[i] = text[i].replace("\n", "")
	
	start_time = time.time()

	characters = string.ascii_lowercase + string.digits
	num_of_char = 0
	while (len(answers) != 15):
		num_of_char += 1
		for attempt in itertools.product(characters, repeat=num_of_char):
			attempt = "".join(attempt)
			result = hashlib.md5(attempt.encode()).hexdigest()
			if result in text:
				answers.append(attempt)
	
	execution_time = time.time() - start_time
	print(execution_time)

with open("ex3_find_plain6.txt", "w") as ans:
	ans.write("\n".join(answers))