from collections import defaultdict

class Solution(object):
	def mostVisitedPatters(self, username, timestamp, website):

		name2site = defaultdict(list)
		seq2names = defaultdict(set)

		# we can merge all list expect ts
		zip_list = list(zip(username, website))

		#we can walk trough 
		for name, site in zip_list:
			
			if name in name2site and len(name2site[name]) >= 2:
				l = len(name2site[name])
				for i in range(l):
					for j in range(i+1,l):
						# and we need one hash map keeping website seq to name. 
						# like
						# (home, about,career): {joe, mary}
						# (home, cart, maps):{james}
						# (home, cart, home):{james}
						# 
						newseq = (name2site[name][i],name2site[name][j], site)
						seq2names[newseq].add(name)

			# we need one hash map keeping name to site 
			# joe : [home, about, career]
			# james: (home, cart, maps, home)
			# mary: (home, about, career)
			# 
			name2site[name].append(site)


		#we just sorted and return first item
		_max = 0
		res = ""
		for k,v in sorted(seq2names.items()):
			if _max < len(v):
				_max = len(v)
				res = k

		return res


username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

res = Solution().mostVisitedPatters(username, timestamp, website)
print(res)


# Output: ["home","about","career"]
