class TreeNode():

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		

def mergeTwoBSTs(root1, root2):

	if not root1 and not root2:
		return None

	#append different list by the inorder traversal
	#merge lists 
	#build tree

	list1 = []
	list2 = []

	#we can use divide - conquer approach. 
	#we have sorted array. we can find mid element and left side less than from mid and right side grater than mid
	def buildBST(list, start, end):
		print("list : ", list)
		print("start : ", start)
		print("end : ", end)

		if start > end:
			return None

		if start == end:
			return TreeNode(list[start])

		mid = (end + start) // 2
		print("mid : ", mid)
		tmp = TreeNode(list[mid])
		tmp.left = buildBST(list, start, mid-1 )
		tmp.right = buildBST(list, mid+1, end )
		return tmp

		
	def mergeTwoList(list1, list2):
		list = []
		i = 0
		j = 0

		while i < len(list1) and j < len(list2):
			if list1[i] <= list2[j]:
				list.append(list1[i])
				i += 1
			else:
				list.append(list2[j])
				j += 1

		while i < len(list1):
			list.append(list1[i])
			i += 1

		while j < len(list2):
			list.append(list2[j])
			j += 1

		return list
		

	def inOrderTraversal(temp, list):
		if not temp:
			return None

		inOrderTraversal(temp.left, list)
		list.append(temp.val)
		inOrderTraversal(temp.right, list)
		return list


	list1 = inOrderTraversal(root1, list1)
	print("list1 : ", list1)
	list2 = inOrderTraversal(root2, list2)
	print("list2 : ", list2)

	merge_list = mergeTwoList(list1, list2)
	print("merge_list : ", merge_list)

	return buildBST(merge_list, 0, len(merge_list)-1)


#uplevel exp data
# 3
# 1
# -1
# 1
# 0
# -1
# 1
# 1
# 2
# 3
# 3
# 1
# -1
# 1
# 0
# -1
# 1
# 6
# 7
# 8


node1 = TreeNode(2)
node1.left =  TreeNode(1)
node1.right = TreeNode(3)


node2 = TreeNode(7)
node2.left =  TreeNode(6)
node2.right = TreeNode(8)

res = mergeTwoBSTs(node1, node2)
print(res.__dict__)
	