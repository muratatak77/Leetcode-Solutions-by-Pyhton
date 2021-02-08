import bisect

def jobScheduling(startTime, endTime, profit):

	zip_list = zip(startTime, endTime, profit)
	print("zip_list : ", zip_list)
	# for item in zip_list:
		# print("item : ", item)

	jobs = sorted(zip_list, key=lambda v: v[1])
	print("jobs merged : ", jobs)

	dp = [[0, 0]]
	for s, e, p in jobs:
		
		print(" s:", s , " / e:", e , "/ p : ", p, " / dp: ", dp)
		print(" we ll send bisect : ", dp," ,",  [s + 1])

		i = bisect.bisect(dp, [s + 1]) - 1
		
		print("  after bisect i : ", i)
		print("     dp[i][1] + p > dp[-1][1]: ",  dp[i][1], "+", p , ">",  dp[-1][1])

		if dp[i][1] + p > dp[-1][1]:
			dp.append([e, dp[i][1] + p])
		print("===============================")
	return dp[-1][1]



startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

res = jobScheduling(startTime, endTime, profit)
print("res : ", res)
