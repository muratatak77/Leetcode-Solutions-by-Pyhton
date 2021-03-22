'''
    Serialize convert to Root object to the string.
        We can use DFS preorder traversal.
        We can start and we can finish most left child means depth.
        like :
            We can check first leaf nodes in the base case. 
                If node is None:
                    we can add to the a result as just 'None' to the global answer array

                else:
                    we can add answer array node.val
                    left recursive 
                    right recursive
                return string

    Deserialize convert to string to the RootObject
        data = '1,2,3,None,None,4,None,None,5,None,None,'
        split(,) > array calling data_list

        if data_list[0] == 'None' # means no child we are in the leaf node
            data_list.pop(0)
            return None

        #recursive case
            root = TreeNode(data_list[0])
            data_list.pop(0)
            left  = dfs(root.left)
            right = dfs(root.right)
            return root



'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None

        def dfs(root):
            #base case, leaf nodes
            if root is None:
                res.append('None')
                return None
            else:
                res.append(str(root.val))
                left = dfs(root.left)
                right = dfs(root.right)            
                
        res = []
        dfs(root)
        print("serialize res : ", res)
        return ','.join(res)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not root:
            return None

        def dfs(l):
            #leaf node
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = dfs(l)
            root.right = dfs(l)
            return root
        
        data_list = data.split(',')
        root = dfs(data_list)
        return root



node = TreeNode(1)
node.left = TreeNode(2)
node.left.left = TreeNode(3)
node.left.right = TreeNode(4)
node.right = TreeNode(5)


def print_tree(root, direction):
    if root is None:
        return None
    else:
        print("root val : ", direction , " - ", root.val,)
        print_tree(root.left, 'left')
        print_tree(root.right, 'right')

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(node))
print("ans : ", print_tree(ans, 'root'))

'''
    T(N) = O(N) , N is number of nodes
    S(N) = O(N) , we have an array and we keep entire tree
'''

