'''
	we need actually custom sorted method. 
	We can use directly sorted method but together some key function.

	logs = ["dig1 8 1 5 1","let1 art can","let2 ar can","dig2 3 6","let2 own kit dig","let3 art zero"]
	
	like  in this array, we have some letter and digits items. 
	if we accross an letter or is alpha chars we can sorted first second part in current item. 
		like : "art can"  in iteration 
		and after we can sort thirth part 'let1' 
	else if we can acroess not alpha character we can sorted just last items.


'''
from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            print("_id : ", _id , "- rest : ",rest)

            if rest[0].isalpha():
            	print("		return 0, rest, _id ", (0, rest, _id) )
            	return (0, rest, _id)  
            else:
            	print("		return 1,", (1, ) )
            	return (1,)

        return sorted(logs, key=get_key)


logs = ["dig1 8 1 5 1","let1 art can","let2 ar can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs = ["1 n u", "r 527", "j 893", "6 14", "6 82"]
res = Solution().reorderLogFiles(logs)
print("res : ", res)

'''
	T(N) = O(M.N.longN ) N : number of logs in the list,  M : maximum length of a single log
	S(N) = O(MN)
'''