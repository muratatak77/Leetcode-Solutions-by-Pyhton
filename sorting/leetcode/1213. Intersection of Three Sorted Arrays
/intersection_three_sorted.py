def arraysIntersection(arr1, arr2, arr3):
	
	# #Hash solution
	dicts = {}

	for key in arr1:
		dicts[key] = 1
		
	for key in arr2:
		if dicts.get(key):
			dicts[key] += 1

	for key in arr3:
		if dicts.get(key):
			dicts[key] += 1

	# return [key for key, val in dicts.items() if val == 3]

#Three pointer solution

    i,j,k = 0,0,0
    res = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            res.append(arr1[i])
            i,j,k = i+1 , j+1, k+1
            continue
		
        max_ = max(arr1[i], arr2[j], arr3[k])
        print(max_)
        if arr1[i] < max_:
            i += 1
        if arr2[j] < max_:
            j += 1
        if arr3[k] < max_:
            k += 1
			
    return res

arr1 = [1,2,3,4,5] 
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
res = arraysIntersection(arr1, arr2, arr3)
print(res)

