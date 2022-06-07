# _source_ https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/2.%20Pattern%20Two%20Pointers/Pair%20with%20Target%20Sum%20(easy).py
# _Topic_ @2 Pattern: Two Pointers
# _Q_ @2. a)
# _Difficulty_ easy

# Problem Statement:
"""
Given an array of sorted numbers and a target sum, 
find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) 
such that they add up to the given target.
Example 1:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""

# brute force: look at all pairs.
# smarter: look at only pairs only up to sum, since list is sorted?
def pair_with_targetsum(arr, target_sum):
	# two forls to point at two items
	for i in range(len(arr)):
		for j in range(len(arr)):
			if i==j:  # pair cannot be the same item twice
				continue
			# if sum is greater than target, no need to continue looking
			if arr[i]+arr[j] > target_sum:
				break
			if arr[i]+arr[j] == target_sum:  # found a pair of indices
				return [i,j]
