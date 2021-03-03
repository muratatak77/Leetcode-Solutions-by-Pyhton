def decode(word, chipper):
	
	hmap = {}

	i = 0
	for number in range(97,123):
		hmap[chr(number)] = cipher[i]
		i+=1

	print(hmap)

	new_str = ""
	for char in word:
		new_str += hmap[char]

	print("new_str : ", new_str)

	return new_str

word = "helloworld"
cipher = "mpgzkeyrsxfwlvjbcnuidhoqat"

res = decode(word, cipher)
