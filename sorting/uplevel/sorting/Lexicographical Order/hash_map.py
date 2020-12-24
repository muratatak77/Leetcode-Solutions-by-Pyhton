#
# Complete the solve function below.
#
def solve(arr):

    sum_map = {}
    val_map = {}
    
    for i in range(len(arr)):
        splt = arr[i].split( )
        key = splt[0]
        value = splt[1]

        if key in sum_map:
            sum_map[key] += 1
            val_map[key] = max(value, val_map[key])
        else:
            sum_map[key] = 1
            val_map[key] = value
        
    
    arr.clear()
    
    for x in sum_map.keys():
        item = x + ":" + str(sum_map[x]) + ":" +val_map[x]
        arr.append(item)
    
    return arr





arr = ["key1 abcd", "key2 zzz", "key1 hello", "key3 world", "key1 hello"]
res = solve(arr)
print(res)
	
		
# ["key1:3,hello",
# "key2:1,zzz",
# "key3:1,world"]