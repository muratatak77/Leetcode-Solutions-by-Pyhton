# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val = 0, left = nil, right = nil)
        @val = val
        @left = left
        @right = right
    end
end
# @param {TreeNode} root
# @return {Integer}
def good_nodes(root)

	@res = 0
	def helper(node, max_val)

		#base case, leaf nodes
		return if node.nil?

		if node.val >= max_val
			@res += 1
		end

		max_val = [max_val, node.val].max

		#recursive case
		#send left and right and max_val
		helper(node.left, max_val) if node.left
		helper(node.right, max_val) if node.right
		
	end

	helper(root,root.val)
	@res

end


root =TreeNode.new(3)
root.left = TreeNode.new(1)
root.left.left = TreeNode.new(3)

root.right = TreeNode.new(4)
root.right.left = TreeNode.new(1)
root.right.right = TreeNode.new(5)

res = good_nodes(root)
puts "res : #{res}"
