class TreeNode():

	def __init__(self, val):
		self.val = val
		self.children = []

def find_height(root):
	
	if not root:
		return 0
  
	maxdepth = 0
	
	for child in root.children:
		maxdepth = max(maxdepth, find_height(child))
		
	return maxdepth + 1



def find_height(root):

    if root is None:
        return 0
    
    max_height = 0
    for child in root.children:
        max_height = max(max_height, 1+find_height(child))
        
    return max_height

    
# children = [3,5,6]
node = TreeNode(1)
node3 = TreeNode(3)
node2 = TreeNode(2)
node4 = TreeNode(4)

node.children.append(node3)
node.children.append(node2)
node.children.append(node4)

node5 = TreeNode(5)
node6 = TreeNode(6)

node3.children.append(node5)
node3.children.append(node6)

result = find_height(node)
print(result)