# shortest substring that is controlling by the set
# O(n^2)

import sys
import copy

def shortestControllingSet(s, _set):
	min = sys.maxsize

	for i in range(len(s)):
		new_set = copy.copy(_set)
		for j in range(i,len(s)):
			if s[j] in new_set:
				new_set.remove(s[j])
				if len(new_set) == 0:
					if min > j-i+1:
						print("Found min. i :", i, " - j : ", j , ".j-i+1 : ", j-i+1)
						min = j-i+1
	return min


s = "helloworld"
_set = {'l', 'r', 'w'}
res = shortestControllingSet(s, _set)

print(res)
