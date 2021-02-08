def sorting(points, k):

	points.sort(key = lambda P: P[0]**2+P[1]**2)
	print(points)
	return points[:k]

points = [[1,3],[-2,2]]
k = 1

res = sorting(points, k)
print(res)