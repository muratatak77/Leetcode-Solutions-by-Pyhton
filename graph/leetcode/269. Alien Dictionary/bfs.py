'''

	words = [
	  "wrt",
	  "wrf",
	  "er",
	  "ett",
	  "rftt"
	]

	- we can compare current word and next word. 
	   wrt
	   wrf

	   we understant t ---> f

	   wrf
	   er

	   w ---> e

	   er
	   ett

	   r ----> t , e --->r
	
	 - generate adjency list
	 - in Directed Acylyc Graph = DAG
     	- Topological sorted order

     		return : 
     		 	w ---> e ---> r ---> t ---> f 

	we need to somehow identify which letters have no incoming links left. 
	We need to check all neighbors for ever each letter. Little to annoying  for first adj list. 
    That why, we need to keep second adj list that it calls indegree adj list.
    indegree count list includes reverse of incoming links of a node. 
    Then each time we traverse an edge, we could remove the corresponding edge in the reverse adj list.
    
    Alg : 

    - First indegree list keeps how many reverse edges there are. We can decrement 1 for each edges. if we have count reach 0 there won't be any edge for current edge.

    - We can apply BFS for all letters that are reachaeble. BFS uses a Queue. 
    	Default we can add to Q all count 0 meaning there is no incoming link.
    	If one letter reach 0 we can add to Q. And we need pull from Q , we can add output list.


    Edges Cases : 
     - if the output doenst include all letter , we can return "" 
     		compare indegree lenght and output length

     - If one word includes own prefix following word there is a other problem. We can not find a valid ordering and we can return ""
     		abcd , abc > we can find valid ordering we can check in is in the loop that compares each adjacent pair of words.

'''


from collections import defaultdict, Counter, deque

def alienOrder(words):
	print("WORDS : ", words)
	
	# Step 0: create data structures + the in_degree of each unique letter to 0.
	adj_list = defaultdict(set)
	print("adj_list :", adj_list)


	# in_degree = Counter({c : 0 for word in words for c in word})
	in_degree = Counter({})
	for word in words:
		for c in word:
			in_degree[c] = 0

	print("in_degree  initial : ", in_degree)
			
	# Step 1: We need to populate adj_list and in_degree.
	# For each pair of adjacent words...
	for first_word, second_word in zip(words, words[1:]):
		print("  first_word :", first_word , " - second_word : ", second_word)

		# merge_letters = zip(first_word, second_word)
		# print("merge_letters : ", tuple(merge_letters))
		# for c1,d1 in merge_letters:
		# 	print("c1 : ", c1)
		# 	print("d1 : ", d1)

		if ((len(second_word) < len(first_word)) and first_word.startswith(second_word)):
			return ""

		for c, d in zip(first_word, second_word):
			print("c : ", c , " - d :", d)
			if c != d:
				if d not in adj_list[c]:
					adj_list[c].add(d)
					in_degree[d] += 1
					print("     Add adj_list :", adj_list)
					print("     Add in_degree :", in_degree)
					print("     ------------------------")
				break
		else:
			if len(second_word) < len(first_word): return ""

	print("Completed adj_list : ", adj_list)
	print("Completed in_degree : ", in_degree)
	print("- -- -- - - - - - - - - - - - - -- - - - - - - - - - - - - -")
	
	# Step 2: We need to repeatedly pick off nodes with an indegree of 0.
	output = []
	queue = deque([c for c in in_degree if in_degree[c] == 0])


	print("Queue initial : ", queue)
	print(" --------------- ")

	while queue:
		c = queue.popleft()
		print("Queue popleft :", c)
		output.append(c)
		print("Output append c :", c, " - output :", output )

		for d in adj_list[c]:
			print("   d in adj_list[c]. d :  ", d, " - c :", c )
			in_degree[d] -= 1
			print("   in_degree =- 1 :", in_degree)
			if in_degree[d] == 0:
				queue.append(d)
				print("      append q : ", queue)
		print(" --------------- ")
				
	# If not all letters are in output, that means there was a cycle and so
	# no valid ordering. Return "" as per the problem description.
	if len(output) < len(in_degree):
		return ""
	# Otherwise, convert the ordering we found into a string and return it.
	return "".join(output)





words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

words = ["x", "y", "x"]

words = ["wxqkj", "whqg", "cckgh", "cdxg", "cdxdt", "cdht", "ktgxt", "ktgch", "ktdw", "ktdc", "jqw", "jmc", "jmg"]


res = alienOrder(words)
print("res : ", res)