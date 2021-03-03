'''
	We can apply a few while loop to compute repeat same sequence number. 
	like n = 4

	we can set a result first 1
		n=4
		res = 1
		new string will be : 11
		res = new_str

		n=3
		res = 11
		new_str will be : 21 
		res = new_str

		n=2
		res=21
		new_str = 12
		- 
		res=11
		new_str will be : 1221 (once 2, twice 1)

		n = 1 
		exit

'''


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
        	return "1"
        #we need an result answer. we can start initial set '1' to result
        res = "1"

        # we can do while loop until n grater than 1. because we have already 1 in  our result.
        while n > 1:
        	print("n :", n)
        	new_str = ""
        	i = 0
        	print("set new_str : ","''", "- i: ", i)
        	#we need second while loop until grater than len result to compute total count repeta of consequence numbers.
        	#like 111
        	#start i = 0 , first digit is 1, finally we will be 3.
        	while i < len(res) :
        		total = 1
        		#we need to walk through if we have the same digits as a sequence.
        		while i+1<len(res) and res[i] == res[i+1]:
        			total += 1
        			i += 1
        		#new string will be 31 after 111
        		print("	total : ", total, " -i:", i)
        		new_str += str(total)+ str(res[i])
        		print("	new_str : ", new_str)
        		i += 1
        		print("	i :", i)
        	n -= 1
        	res = new_str
        return res


n = 6
res = Solution().countAndSay(n)
print("res : ", res)

'''
	1 - 11
	2 - 21
	3 - 21
	4 - 1211
	5 - 111221

	
	T(N) = O(N^2) because  we could assume that is the worst case, the lenght of the sequence would grow exponentialy.
	S(N) = O(N^2-1) 
	