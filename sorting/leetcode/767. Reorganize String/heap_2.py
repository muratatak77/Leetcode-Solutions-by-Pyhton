import heapq
class Solution(object):
	def reorganizeString(self, S):

		#we need to keep count chars by using a set
		#like aba case : we need sort this way ((-2,a), (-1,b))
		#and we can put the heap 

		# and we need pop from heap. After pop if there is no char to process we can exit while iterator 
		# 

		pq = []
		for x in set(S):
			pq.append((-S.count(x),x))
		print("pq : ", pq)

		#initial the heap
		heapq.heapify(pq)

		#we have some edge case like :   
		#	if freq > (N+1)/2  return empty
		#		if abaa case : freq = 3a, 1b
		#		freq = -(-3) > (4+1)/2  = 2.5 case is not impossible we can return empty
		for freq,char in pq:
			if -freq > (len(S)+1)/2:
				return ""

		ans = []
		while len(pq) >= 2:
			#heap = ((-2,a), (-1,b))
			freq1, char1 = heapq.heappop(pq)
			freq2, char2 = heapq.heappop(pq)
			#heap : ()
			#freq1 : 2 char :1 
			ans.extend([char1,char2])
			#ans : [a,b]
			
			if freq1 + 1:
				heapq.heappush(pq, (freq1+1, char1))
				#(-1,a)
				
			if freq2 +1:
				heapq.heappush(pq, (freq2+1, char2))

		res = "".join(ans)
		if pq:
			res += pq[0][1]

		return res



S = "abacdaa"
res = Solution().reorganizeString(S)
print("res : ", res)


			





