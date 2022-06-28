# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/7.%20Pattern%20Breath%20Depth%20First%20Search/Binary%20Tree%20Level%20Order%20Traversal%20(easy).py
# _Topic_ @7 Pattern: In-place Reversal of a LinkedList
# _Q_ @7. a)
# _Difficulty_ easy
# my_sol in 10 mins but I doubt it runs...

# Problem Statement
"""
Problem Statement 
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level from left 
to right in separate sub-arrays.
"""

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
	# array
	tree_array = []
	# use BFS
	queue = [root]
	while len(queue) != 0:
		# find children, add to queue
		# add to array, contiue?
		current = queue.pop()
		tree_array.append(current)
		if current.left is not None:
			queue.append(current.left)
		if current.right is not None:
			queue.append(current.right)

	return tree_array
