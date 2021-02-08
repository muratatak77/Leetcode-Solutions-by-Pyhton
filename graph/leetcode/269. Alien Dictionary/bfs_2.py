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


from collections import defaultdict, deque, Counter

def alienOrder(words):

	# x > {h,c}
	adj_list = defaultdict(set)

	# x : 0,c: 2 ...
	in_degree =  Counter({})
	for word in words:
		for letter in word:
			in_degree[letter] = 0


	# fill adj list and in_degree
	for first_word, sec_word in zip(words, words[1:]):

		#edge cases , 
		#like abcd , abc we can find a valid order in this case
		if len(sec_word) < len(first_word) and first_word.startswith(sec_word):
			return ""

		for l1, l2 in zip(first_word, sec_word):
			if l1 != l2:
				if l2 not in adj_list[l1]:
					adj_list[l1].add(l2)
					in_degree[l2] += 1
				break

	print("adj_list : ", adj_list)
	print("in_degree : ", in_degree)

	q = deque([])
	for letter in in_degree:
		if in_degree[letter] == 0:
			q.append(letter)

	print("q : ", q)

	output = []

	while q:
		node = q.popleft()
		output.append(node)
		for nei in adj_list[node]:
			in_degree[nei] -= 1
			if in_degree[nei] == 0:
				q.append(nei)

	#edge case
	if len(output) < len(in_degree):
		return ""

	print("output: ", output)

	return "".join(output)


words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

# words = ["x", "y", "x"]

words = ["wxqkj", "whqg", "cckgh", "cdxg", "cdxdt", "cdht", "ktgxt", "ktgch", "ktdw", "ktdc", "jqw", "jmc", "jmg"]


res = alienOrder(words)
print("res : ", res)


'''
 N : number of total strings in the input list
 C : total lenght of all the words in the input list
 U : total number of unique letters in the alien alphabet

 	T(N) = O(C)
 	    BFS : O(V+E) => V : number of vertices , E is number of edges
 	    O(U) = There is a one vertex for each char
 	    	



 T
'''