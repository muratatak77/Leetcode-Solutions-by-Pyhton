def overall(n):

	result = []

	def nonConflict(slate, col):
		print("============== start nonConflict =============== ")
		print("slate : ", slate, " - col :", col)
		for q in range(len(slate)):
			print("             q : " , q)
			if slate[q] == col:
				print("            slate[q] == col return False ")
				return False
			rowdiff = abs(len(slate) - q)
			coldiff = abs(col-slate[q])
			print("               rowdiff == coldiff. ", rowdiff , " == ", coldiff)
			if rowdiff == coldiff:
				return False
		print("                  end nonConflict - return True =============== ")
		return True


	def helper(slate,i,n):
		print("helper slate : ", slate , " - i : ", i)
		if i == n:
			print("    slate appended : ", slate[:])
			result.append(slate[:])
			return

		for col in range(0,n):
			is_nonconflict = nonConflict(slate, col)
			print("   is_nonconflict :" , is_nonconflict, " - col :", col)
			if is_nonconflict:
				print("   before append col : ", col, " - i : ", i)
				slate.append(col)
				print("   after append slate : ", slate)

				helper(slate, i+1,n)
				print("        --- slate pop ---")
				slate.pop()



	helper([],0,n)
	return result

res = overall(4)
print("res : ", res)