def minDistance(word1, word2):

	w2size = len(word2)
	w1size = len(word1)

	# for row in range(1+w2size):
		# for col in range(1+w1size):
			# table[row][col] = 0


	table = [ [0 for _ in range(1+w2size)] for _ in range(1+w1size) ]
	print("Initial Table : ",  table)

	for col in range(1,1+w2size):	
		table[0][col] = col

	for row in range(1,1+w1size):
		table[row][0] = row

	print("Initial Table :col - row ",  table)

	for row in range(1,1+w1size):
		for col in range(1,1+w2size):
			if word1[row-1] == word2[col-1]:
				s = 0
			else:
				s = 1
			table[row][col] = min(table[row-1][col]+1, table[row][col-1]+1, table[row-1][col-1]+s)

	return table[-1][-1]


word1 = "horse"
word2 = "ros"

ans = minDistance(word1, word2)
print(ans)