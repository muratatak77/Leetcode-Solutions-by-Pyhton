from collections import defaultdict
from collections import Counter
import itertools

class Solution:
	def mostVisitedPattern(self, username, timestamp, website):

		graph = defaultdict(list)

		zip_list = zip(username, timestamp, website)
		zip_list = sorted(zip_list)

		print("zip_list: ", zip_list)

		for u, t, w in zip_list:
			graph[u].append(w)

		print("graph : ", graph)
		print("graph items : ", graph.items())
		
		counter = Counter()

		for u, routes in graph.items():

			

			for triple in set(itertools.combinations(routes, 3)):
				counter[triple]+=1
		
		print("counter : ", counter)



		pattern, count = None, 0
		for pat, c in counter.items():
			if c > count:
				pattern = pat
				count = c
			elif c == count and pattern > pat:
				pattern = pat
				
		return pattern


username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

res = Solution().mostVisitedPattern(username, timestamp, website)
print("res ; ", res)
