
# 
# Your previous Plain Text content is preserved below:
# 
# 
# 
# +------------+
# | JOB | DEPS |
# | ---------- |
# | A   | B, C |
# | B   | D, E, F |
# | C   | B    |
# | D   |      |
# | E   |      |
# | F   |      |
# +------------+
# 
#               A           
#       
#         B          C  

#     D   E   F    B
		  
# 
# 
# hmap = {A : [B,C], B: [D,E], C: [B], D:[], E:[], F: []}
# 
# [D, E, B, C, A, F]
# [D, E, F, B, C, A]



class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.children = []

class Solution(object):
	def getOutput(self, node):
		
		result = []
		
		def dfs(node):

			print("NODE : ", node)

			#base case
			if not node.children:
				if node.val not in result:
					result.append(node.val)
					return

			for nod in node.children:
				dfs(nod)
				if nod.val not in result:
					result.append(nod.val)


		dfs(node)
		return result


node = TreeNode("A")
nodeB = TreeNode("B")
nodeC =  TreeNode("C")

node.children = [nodeB, nodeC]

nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeB.children = [nodeD, nodeE, nodeF]

print("Node : ", node)
res = Solution().getOutput(node)
print("res : ", res)



	
	

