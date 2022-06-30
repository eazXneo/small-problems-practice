# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/7.%20Pattern%20Breath%20Depth%20First%20Search/Binary%20Tree%20Level%20Order%20Traversal%20(easy).py
# _Topic_ @8 Pattern: Tree Depth First Search
# _Q_ @8. a)
# _Difficulty_ easy
# Time taken until for own solution, without compiling the code: 15 min

# Problem Statement
"""
Given a binary tree and a number ‘S’, 
find if the tree has a path from root-to-leaf such that the sum of all the 
node values of that path equals ‘S’.
"""

# from answer
class TreeNode:
 	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
# My solution:
# worst case binary tree is a LL
# use DFS to find all paths from root to leaf
# use stack (or recursion I guess)
def has_path(root, sum):  # from Q I guess it returns boolean.
	stack = [root]
	current_sum = 0
	while len(stack) != 0:
		current_node = stack.pop()
		# update current_sum:
		current_sum += current_node.val

		if current_sum == sum:
			return True
		if current_node.left is not None:
			stack.append(current_node.left)
		elif current_node.right is not None:
			stack.append(current_node.right)
		else:  # trying to backtrack with the total sum
			current_sum -= current_node.val
	return False 
# deque vs list rep...?
# idea for recursion is has_path_rec(root, sum)
# base case, root has no children. return if sum = root.val
# base case as well? if root is None, return False
# keep calling has_path_rec(root, sum-curr.val) for left AND
# 	right children
