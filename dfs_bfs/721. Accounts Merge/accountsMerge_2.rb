# '''
# accounts = [
	
# 	["John", "johnsmith@mail.com", "john00@mail.com"], 
# 	["John", "johnnybravo@mail.com"], 
# 	["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
# 	["Mary", "mary@mail.com"]]

# Result :

# 	[

# 	["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  
# 	["John", "johnnybravo@mail.com"], 
# 	["Mary", "mary@mail.com"]]

# ----------------------------------------------------------------------------

# Solving :


# We need to connect each email goes to another emails , generate a graph like neighbors list
# Connections between email list like a graph adjacent list

# We can seperate 2 cases 
# 1. Constructer graph and email to name hash map relation
# 	Graph : 
# 	{
# 		 'johnsmith@mail.com': {'john_newyork@mail.com', 'john00@mail.com', 'johnsmith@mail.com'},
# 		 'john00@mail.com': {'johnsmith@mail.com'}, 
# 		 'johnnybravo@mail.com': {'johnnybravo@mail.com'}, 
# 		 'john_newyork@mail.com': {'johnsmith@mail.com'}, 
# 		 'mary@mail.com': {'mary@mail.com'}
# 	}
# 	
# 	{
# 	"johnsmith@mail.com"=>#<Set: {"johnsmith@mail.com", "john_newyork@mail.com"}>, "
# 	john00@mail.com"=>#<Set: {"johnsmith@mail.com", "john00@mail.com"}>, 
# 	"johnnybravo@mail.com"=>#<Set: {"johnnybravo@mail.com"}>, 
# 	"john_newyork@mail.com"=>#<Set: {"johnsmith@mail.com", "john_newyork@mail.com"}>, 
# 	"mary@mail.com"=>#<Set: {"mary@mail.com"}>
# 	}
# 	

# 	we will generate together email_to_name hashmap

# 	email_to_name :{
# 					'johnsmith@mail.com': 'John', 
# 					'john00@mail.com': 'John', 
# 					'johnnybravo@mail.com': 'John', 
# 					'john_newyork@mail.com': 'John', 
# 					'mary@mail.com': 'Mary'
# 				}

# 2. we can apply BFS - Bread First Search.
# 	We can use a stack keep and to find graph edge and neighbours.
# 	We can add a compnonent array for  email and  in the each level neighbours.

# '''

require 'set'

def accountsMerge(accounts)
	graph = {}

	email_to_name = {}

	accounts.each do |acc|
		# puts ""
		# print " ACC : ", acc
		name = acc[0]
		# puts ""
		# print "name : ", name
		# puts ""
		# print("  acc[1,acc.size+1] : ", acc[1,acc.size+1])
		# puts ""

		graph_set = Set.new()
		acc[1,acc.size+1].each do |email|
			# print " 	/ acc[1] > ", acc[1]
			# puts ""
			# print " 	/ email] > ", email
			# puts ""
			graph[acc[1]] = graph_set.add(email)
			graph[email] = graph_set.add(acc[1])
			email_to_name[email] = name
		end
	end

	print("graph :", graph)

	graph["johnsmith@mail.com"].each do |ss|
		puts "ss : ", ss
	end

	seen ={}
	ans = []

	puts ""
	puts ""
	puts ""

	graph.keys.each do |email|
		print  " >>> email : ", email
		puts ""
		if seen.include?(email)
			next
		end

		seen[email]=1
		stack = []
		stack.append(email)
		components = []
		puts ""
		print  " >>> seen : ", seen
		puts ""

		print  " >>> stack : ", stack.size

		while stack && stack.size > 0 do
			node = stack.shift()
			components.append(node)
			puts ""
			print("node : ", node)
			puts ""
			
			print("graph[node] : ", graph[node])


			graph[node].each do |nei|
				print(" nei : ", nei)
				puts ""

				if seen[nei] == 1
					next
				end

				break

				seen[email]=1
				stack.append(nei)
				
				puts ""
				print("stack : ", stack)
				
	
			end
		end

		ans.append([email_to_name[email]] + components.sort())
		puts""
		print("seen :", seen)
		puts""
		print("ans : ", ans)
		return ans

	end

end




# GRAPH :  defaultdict(<class 'set'>, {'johnsmith@mail.com': {'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'}, 'john00@mail.com': {'johnsmith@mail.com'}, 'johnnybravo@mail.com': {'johnnybravo@mail.com'}, 'john_newyork@mail.com': {'johnsmith@mail.com'}, 'mary@mail.com': {'mary@mail.com'}})
# em_to_name :  {'johnsmith@mail.com': 'John', 'john00@mail.com': 'John', 'johnnybravo@mail.com': 'John', 'john_newyork@mail.com': 'John', 'mary@mail.com': 'Mary'}




# class Solution(object):
# 	def accountsMerge(self, accounts):

# 		# generate a graph  adjacent list and  email to name hash map
# 		graph = defaultdict(set)
# 		email_to_name = {}

# 		for acc in accounts:
# 			name = acc[0]
# 			for email in acc[1:]:
# 				graph[acc[1]].add(email)
# 				graph[email].add(acc[1])
# 				email_to_name[email] = name

# 		print("graph : ", graph)

# 		#BFS get neighbours and add global ans components
# 		seen = set()
# 		ans = []
# 		for email in graph:
# 			if email in seen:
# 				continue

# 			seen.add(email)

# 			stack = [email]
# 			components = []
# 			while stack:
# 				node = stack.pop()
# 				components.append(node)
# 				for nei in graph[node]:
# 					if nei not in seen:
# 						seen.add(nei)
# 						stack.append(nei)
# 			ans.append([email_to_name[email]] + sorted(components))

# 		return ans



accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
res = accountsMerge(accounts)
puts ""
puts ""
print("res : ", res)