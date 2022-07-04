# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/7.%20Pattern%20Breath%20Depth%20First%20Search/Binary%20Tree%20Level%20Order%20Traversal%20(easy).py
# _Topic_ @7 Pattern: Breath Depth First Search
# _Q_ @7. a)
# _Difficulty_ easy
# my_sol in 10 mins but I doubt it runs...

# Problem Statement
"""
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level from left 
to right in separate sub-arrays.
"""

# My solution:
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

def MY_traverse(root):
	# array
	tree_array = []
	# use BFS
	queue = [root]
	while len(queue) != 0:
		# find children, add to queue
		# add to array, contiue?
		current = queue.pop(0)
		tree_array.append(current.val)
		if current is None:
			continue
		if current.left is not None:
			queue.append(current.left)
		# else:
		# 	tree_array.append(None)
		if current.right is not None:
			queue.append(current.right)
		# else:
		# 	tree_array.append(None)

	return tree_array

## ANSWER
from collections import deque

def traverse(root):  # looks a bit more professional
	result = []
	if root is None:
		return result

	queue = deque()  # use deque as queue DS...
	queue.append(root)
	while queue:
		levelSize = len(queue)
		currentLevel = []
		for _ in range(levelSize):
			currentNode = queue.popleft()
			# add the node to the current level
			currentLevel.append(currentNode.val)
			# insert the children of current node in the queue
			if currentNode.left:
				queue.append(currentNode.left)
			if currentNode.right:
				queue.append(currentNode.right)
		result.append(currentLevel)

	return result

""" Asymptotics:
For sols: O(n) <- accesses each node of the tree once and appends it to the array
For mine: O(n) <- should also look at each element in tree once.
Space complexity: O(n) <- need to store all values in tree in array of length 'n'
	(Also queue takes at much n/2 space and so O(n) space for the queue too.)
"""


# Additional code
def main():  # my answer does not have additional lists for levels. Otherwise looks ok.
	print("My answer:")
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Level order traversal: " + str(MY_traverse(root)))

	print("Solutions:")
	root2 = TreeNode(12)
	root2.left = TreeNode(7)
	root2.right = TreeNode(1)
	root2.left.left = TreeNode(9)
	root2.right.left = TreeNode(10)
	root2.right.right = TreeNode(5)
	print("Level order traversal: " + str(traverse(root2)))
	
main()
