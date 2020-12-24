def test(first = 0):
	print("call test. first :", first)
	if first == 2:
		print("return first :", first)
		print("===========")
		return

	for i in range(0,2):
		print("i : ", i, " - first : " , first)
		test(first+1)
		# print("after i : ", i)

		
test()
