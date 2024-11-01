import string


frequency = {}
text = ""
with open("story_cipher.txt", mode="r") as t:
	text = t.read()
	for char in string.printable:
		frequency[char] = 0
	for char in text:
		frequency[char] += 1

	sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
	to_remove = []
	for tuple in sorted_frequency:
		if tuple[0] in {" ", ",", "."}:         ## " " is preserved, "," is temporarily ignored, "." is temporarily ignored
			to_remove.append(tuple)
	for tuple in to_remove:
		sorted_frequency.remove(tuple)
	
	## [('U', 305), ('J', 263), ('Y', 229), ('Q', 213), ('E', 206), ('D', 205), ('I', 198), ('X', 160), ('H', 131), ('B', 102),
	## ('T', 98), ('W', 71), ('C', 70), ('S', 61), ('O', 58), ('K', 51), ('M', 50), ('V', 50), ('F', 43), ('R', 35), ('L', 29),
	## ('A', 20), ('N', 3), ('Z', 3), ('P', 1), ('0', 0), ('1', 0), ('2', 0), ('3', 0), ('4', 0), ('5', 0), ('6', 0), ('7', 0),
	## ('8', 0), ('9', 0), ('a', 0), ('b', 0), ('c', 0), ('d', 0), ('e', 0), ('f', 0), ('g', 0), ('h', 0), ('i', 0), ('j', 0),
	## ('k', 0), ('l', 0), ('m', 0), ('n', 0), ('o', 0), ('p', 0), ('q', 0), ('r', 0), ('s', 0), ('t', 0), ('u', 0), ('v', 0),
	## ('w', 0), ('x', 0), ('y', 0), ('z', 0), ('G', 0), ('!', 0), ('"', 0), ('#', 0), ('$', 0), ('%', 0), ('&', 0), ("'", 0),
	## ('(', 0), (')', 0), ('*', 0), ('+', 0), ('-', 0), ('/', 0), (':', 0), (';', 0), ('<', 0), ('=', 0), ('>', 0), ('?', 0),
	## ('@', 0), ('[', 0), ('\\', 0), (']', 0), ('^', 0), ('_', 0), ('`', 0), ('{', 0), ('|', 0), ('}', 0), ('~', 0), ('\t', 0),
	## ('\n', 0), ('\r', 0), ('\x0b', 0), ('\x0c', 0)]

	## original cipher frequency list
	## cipher_frequency_list = ["U", "J", "Y", "Q", "E", "D", "I", "X", "H", "B", "T", "W", "C", "S", "O", "K", "M", "V", "F", "R", "L", "A", "N", "Z", "P", "G"]
	## manually adjusted frequency list
	cipher_frequency_list = ["U", "J", "Q", "E", "Y", "D", "I", "H", "X", "B", "T", "S", "K", "C", "V", "F", "W", "M", "O", "R", "L", "A", "N", "Z", "P", "G"]
	## list sorted based on frequency of letters in an English Corpus
	usual_frequency_list = ["e", "t", "a", "o", "i", "n", "s", "r", "h", "l", "d", "c", "u", "m", "f", "p", "g", "w", "y", "b", "v", "k", "x", "j", "q", "z"]
	
	for i in range(len(usual_frequency_list)):
		text = text.replace(cipher_frequency_list[i], usual_frequency_list[i])
	
file_path = "solution.txt"
with open(file_path, mode="w") as f:
		f.write(text)

print(text)