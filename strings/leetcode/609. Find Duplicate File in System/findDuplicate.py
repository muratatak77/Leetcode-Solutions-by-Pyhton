'''
	we can walk trough iterate paths.
	we need path name and content 
	we need a hash map .would be key : content , value : path
	
	like : 
		["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]

		key : abcd . val : [root/a/1.txt, root/c 3.txt]
		so on ...

	first we can split(" ") each item :   root/a,1.txt(abcd),2.txt(efgh)
		and each path first item will be path = root/a
		next items will be file and content
			we can get content from between parantheses. we can split first "(" char  ===>  root/a,1.txt,abcd) and we can replace second char ")" with the empty string
			will be :
			let's call name_cont = [1.txt,abcd]

'''
from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        if not paths:
        	return []

        hmap = defaultdict(list)

        for path in paths:
        	values = path.split(" ")

        	for i in range(1,len(values)):
        		name_cont = values[i].split("(")
        		name_cont[1] = name_cont[1].replace(")", "")
        		hmap[name_cont[1]].append(values[0]+"/"+name_cont[0])

        res = []
        for val in hmap.values():
        	if len(val) > 1:
        		res.append(val)


        return res


paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
# paths = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]

res = Solution().findDuplicate(paths)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("res :", res)

'''
	T(N) = O(N*X) N strings of avarage length X is parsed. 
	S(N) = O(N*X) map and res size grow up to N*X


========================================
========================================
example

paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]


	path :  root/a 1.txt(abcd) 2.txt(efgh)
	values :  ['root/a', '1.txt(abcd)', '2.txt(efgh)']
		name_cont 1:  ['1.txt', 'abcd)']
		name_cont 2:  ['1.txt', 'abcd']
 		hmap :  defaultdict(<class 'list'>, {'abcd': ['root/a/1.txt']})
========================================
		name_cont 1:  ['2.txt', 'efgh)']
		name_cont 2:  ['2.txt', 'efgh']
 		hmap :  defaultdict(<class 'list'>, {'abcd': ['root/a/1.txt'], 'efgh': ['root/a/2.txt']})
========================================
	path :  root/c 3.txt(abcd)
	values :  ['root/c', '3.txt(abcd)']
		name_cont 1:  ['3.txt', 'abcd)']
		name_cont 2:  ['3.txt', 'abcd']
 		hmap :  defaultdict(<class 'list'>, {'abcd': ['root/a/1.txt', 'root/c/3.txt'], 'efgh': ['root/a/2.txt']})
========================================
	path :  root/c/d 4.txt(efgh)
	values :  ['root/c/d', '4.txt(efgh)']
		name_cont 1:  ['4.txt', 'efgh)']
		name_cont 2:  ['4.txt', 'efgh']
 		hmap :  defaultdict(<class 'list'>, {'abcd': ['root/a/1.txt', 'root/c/3.txt'], 'efgh': ['root/a/2.txt', 'root/c/d/4.txt']})
========================================
	path :  root 4.txt(efgh)
	values :  ['root', '4.txt(efgh)']
		name_cont 1:  ['4.txt', 'efgh)']
		name_cont 2:  ['4.txt', 'efgh']
 		hmap :  defaultdict(<class 'list'>, {'abcd': ['root/a/1.txt', 'root/c/3.txt'], 'efgh': ['root/a/2.txt', 'root/c/d/4.txt', 'root/4.txt']})
========================================
result generate from hash map values:  [['root/a/1.txt', 'root/c/3.txt']]
result generate from hash map values:  [['root/a/1.txt', 'root/c/3.txt'], ['root/a/2.txt', 'root/c/d/4.txt', 'root/4.txt']]
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

res : [['root/a/1.txt', 'root/c/3.txt'], ['root/a/2.txt', 'root/c/d/4.txt', 'root/4.txt']]


'''