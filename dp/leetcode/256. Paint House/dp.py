def minCost(costs):

	#edge cases
	if not costs:
		return 0

	if len(costs) == 0:
		return 0

	#base cases
	red = [0 for _ in range(len(costs))]
	blue = [0 for _ in range(len(costs))]
	green = [0 for _ in range(len(costs))]
	
	red[0] = costs[0][0]
	blue[0] = costs[0][1]
	green[0] = costs[0][2]
	
	print("red : ", red)
	print("blue : ", blue)
	print("green : ", green)

	for i in range(1, len(costs)):
		red[i] += costs[i][0] + min(blue[i-1], green[i-1])
		# print("   red[i]: ", red[i])
		blue[i] += costs[i][1] + min(red[i-1], green[i-1])
		green[i] += costs[i][2] + min(blue[i-1], green[i-1])


	print("	red 2 : ", red)
	print("	blue 2: ", blue)
	print("	green 2: ", green)

	return min(red[-1], blue[-1], green[-1])


costs = [[17,2,17],[16,16,5],[14,3,19]]
ans = minCost(costs)
print("ans : ", ans)