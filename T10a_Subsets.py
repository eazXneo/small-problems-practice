# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/10.%20Pattern%20Subsets/Subsets%20(easy).py
# _Topic_ @10 Pattern: Subsets
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
def MY_find_subsets(nums):  # really good, good job.
	# recursion?
	# floop?
	all_subsets = [[]]
	for number in range(len(nums)):
		current_level = all_subsets
		for j in range(len(current_level)):
			all_subsets.append(current_level[j]+[nums[number]])

	return all_subsets

# ANSWER
def find_subsets(nums):
	subsets = []
	# start by adding the empty subset
	subsets.append([])
	for currentNumber in nums:
		# we will take all existing subsets and insert the current number in them to create new subsets
		n = len(subsets)
		for i in range(n):
			# create a new subset from the existing subset and insert the current element to it
			set = subsets[i].copy()
			set.append(currentNumber)
			subsets.append(set)
	return subsets

""" Asymptotics:
For sols: O(2^n), where 'n' is the length of 'nums'. Each level doubles the number of already 
	existing elements.
For mine: O(2^n), hopefully.
Space complexity: O(2^n), to hold all combinations.
"""


# Additional code
def main():
	print("My answer:")
	print("Here is the list of subsets: " + str(MY_find_subsets([1, 3])))
	print("Here is the list of subsets: " + str(MY_find_subsets([1, 5, 3])))

	print("Solutions:")
	print("Here is the list of subsets: " + str(find_subsets([1, 3])))
	print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))

main()
