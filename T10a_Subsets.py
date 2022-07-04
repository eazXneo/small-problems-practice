# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/10.%20Pattern%20Subsets/Subsets%20(easy).py
# _Topic_ @9 Pattern: Subsets
# _Q_ @10. a)
# _Difficulty_ easy
# Time taken until for own solution, without compiling the code: 20 min

# Problem Statement
"""
Given a set with distinct elements, find all of its distinct subsets.
Example 1:
Input: [1, 3]
Output: [], [1], [3], [1,3]
Example 2:
Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""

# My solution
def find_subsets(nums):
	# recursion?
	# floop?
	all_subsets = [[]]
	for number in range(len(nums)):
		current_level = all_subsets
		for j in range(len(current_level)):
			all_subsets.append(current_level[j]+[nums[number]])

	return all_subsets
