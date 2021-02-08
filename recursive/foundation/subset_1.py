def subsets(n):
	if n == 0:
		return 1
	else:
		sbs = 2*(subsets(n-1))
		print(sbs)
		return sbs

def subsets_2(n):
	if n == 0:
		return 1
	else:
		sbs = subsets_2(n-1) + subsets_2(n-1) 
		print(sbs)
		return sbs



subsets_2(3)
