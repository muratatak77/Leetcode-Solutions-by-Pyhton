def check_attend(intervals):

	intervals.sort() # O(Nlongn)
	print(intervals)

	for i in range(len(intervals) - 1):     # O(n)
		if intervals[i][1] > intervals[i+1][0]:
			return False
	return True


# h = [[0,30],[1,10],[15,20]]
h = [[4,8],[1,2],[9,12]]

res = check_attend(h)
print(res)