def check_attend(intervals):
	
	intervals.sort()
	for i in range(len(intervals)-1):
		if intervals[i][1]>intervals[i+1][0]:
			return False

	return True


intervals = [[0,30], [5,10],[15,20]]
intervals = [[7,10], [2,4]]

res = check_attend(intervals)
print(res)
