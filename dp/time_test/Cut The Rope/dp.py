def max_product_from_cut_pieces(n):
	
	if n < 2 or n > 110:
		return 0

	table = [0] * (n+1)
	table[1] = 1

	for i in range(2,n+1):
		if i == n:
			best = n-1
		else:
			best = i

		for j in range(1,i):
			print("best : ", best)
			print("table[j] * table[i-j] : ", table[j] * table[i-j])
			if table[j] * table[i-j] > best:
				best = table[j] * table[i-j]
		table[i] = best

	return table[n]



n = 4
ans = max_product_from_cut_pieces(n)
print(ans)
