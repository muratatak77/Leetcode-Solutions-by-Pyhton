import heapq
class Solution(object):
	def reorganizeString(self, S):
		
		# we need to sort according the count
		# we can process with the negative numbers , after we can add plus +1 and if we reach the zero meaning we spend all relevant chars and we should not any process currently char
		pq = []
		for x in set(S):
			pq.append((-S.count(x),x))

		# pq = [(-S.count(x), x) for x in set(S)]
		# for aba : pq will be : [(-2, 'a'), (-1, 'b')]
		print("pq : ", pq)

		#put the heap :  [(-2, 'a'), (-1, 'b')]
		heapq.heapify(pq)

		#if freq grater than (len(S)+1)/2 that it cannot be posibble.
		#
		#like abaa : [(-3, 'a'), (-1, 'b')]
		# N = 4+1 = 5 / 2 = 2/5.
		# freq : 3 > 2.5 we dont need to continue return empty
		for freq, char in pq:
			print("freq : ", freq , " / char : ", char)
			if -freq > (len(S)+1)/2:
				return ""

		# if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
			# return ""

		ans = []
		while len(pq) >= 2:
			freq1, ch1 = heapq.heappop(pq)
			freq2, ch2 = heapq.heappop(pq)
			#freq1 = -2 , ch1 = a
			#freq2 = -1,  ch1 = b
			print("freq1 : ", freq1, " / ch1 :", ch1)
			print("freq2 : ", freq2, " / ch2 :", ch2)
			print("len pq : ", len(pq))
			#This code turns out to be superfluous, but explains what is happening
			#if not ans or ch1 != ans[-1]:
			#    ans.extend([ch1, ch2])
			#else:
			#    ans.extend([ch2, ch1])
			ans.extend([ch1, ch2])
			#ans will be ['a', 'b']
			print("ans : " , ans)
			print("freq1 + 1 : ", freq1 + 1)
			# we need to check is there any chars to check
			# if we have no zero from freq1+1 we can continue add the heap and check again
			if freq1 + 1:
				print("hii freq1 + 1")
				heapq.heappush(pq, (freq1 + 1, ch1))
				#will be after heappush [(-1, 'a')]
				print("after heappush : ", pq)

			print("freq2 + 1 : ", freq2 + 1)
			# in [(-2, 'a'), (-1, 'b')] case we dont have no longer (-1, 'b') 
			# freq2 + 1 = 0
			if freq2 + 1: 
				print("hii freq2 + 1")
				heapq.heappush(pq, (freq2 + 1, ch2))


		print("ans : ", ans)
		print("pq : ", pq)
		
		res = "".join(ans)
		if pq:
			res += pq[0][1]
		return res

		# return "".join(ans) + (pq[0][1] if pq else '')


s="aabaa"
res = Solution().reorganizeString(s)


print("res : ", res)