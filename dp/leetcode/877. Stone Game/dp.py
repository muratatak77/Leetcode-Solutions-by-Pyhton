def stoneGame(piles):
	
	print("size piles : ", len(piles))
	table = [ [False] * len(piles) for _ in range(len(piles))]
	print("Initial table : ", table)

	for diag in range(len(piles)):
		table[diag][diag] = True
	
	print("base case table : ", table)


	for row in range(len(piles)-2,-1,-1):
		print("start for row :", row)
		for col in range(diag, len(piles)):
			print("start for row - col :",row,",",col )
			print("table[row][col-1] : ", table[row][col-1] , " Row : ", row, "  - Col : ", col-1)
			if table[row][col-1] == False:
				print("table[row][col] = True, - Row : ",row , " - Col : ", col)
				table[row][col] = True
			print("table[row+1][col] : ", table[row+1][col] , " Row : ", row+1, "  - Col : ", col)
			if table[row+1][col] == False:
				table[row][col] = True
				print("table[row][col] = True, - Row : ",row , " - Col : ", col)

	print("Finally Table : ", table)

	return table[0][len(piles)-1]


piles = [5,3,4,5]
ans = stoneGame(piles)
print(ans)