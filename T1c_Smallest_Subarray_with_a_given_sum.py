# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/1.%20Pattern%20Sliding%20Window/Smallest%20Subarray%20with%20a%20given%20sum%20(easy).py
# _Topic_ @3 Pattern: Sliding Window
# _Q_ @1. c)
# _Difficulty_ easy

# Problem statement:
"""
Given an array of positive numbers and a positive number ‘S’, 
find the length of the smallest contiguous subarray whose
sum is greater than or equal to ‘S’. 
Return 0, if no such subarray exists.
Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are 
[3, 4, 1] or [1, 1, 6].
"""

# My solution:
import math
def smallest_subarray_with_given_sum(s, arr):
	curr_subarr = [arr[0]]
	# wind_start = 0
	shortest_subarr_len = 0
	for wind_end in range(1, len(arr)):
		curr_subarr.append(wind_end)
		if sum(curr_subarr) >= s:
			if len(curr_subarr) < shortest_subarr_len:
				shortest_subarr_len = len(curr_subarr)
			else:
				curr_subarr.pop(0)
				# wind_start += 1

	return shortest_subarr_len
