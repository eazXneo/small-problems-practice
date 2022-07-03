# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/1.%20Pattern%20Sliding%20Window/Smallest%20Subarray%20with%20a%20given%20sum%20(easy).py
# _Topic_ @3 Pattern: Sliding Window
# _Q_ @1. b)
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
def MY_smallest_subarray_with_given_sum(s, arr):
	curr_subarr = [arr[0]]
	# wind_start = 0
	shortest_subarr_len = math.inf  # in sols it's =math.inf
	for wind_end in range(1, len(arr)):
		curr_subarr.append(arr[wind_end])
		while sum(curr_subarr) >= s:
			if len(curr_subarr) < shortest_subarr_len:
				shortest_subarr_len = len(curr_subarr)
				curr_subarr.pop(0)
			else:
				curr_subarr.pop(0)
				# wind_start += 1
	if shortest_subarr_len == math.inf:  # needed from sols I think.
		return 0
	return shortest_subarr_len

## ANSWER:
def smallest_subarray_with_given_sum(s, arr):
	window_sum = 0
	min_length = math.inf
	window_start = 0

	for window_end in range(0, len(arr)):
		window_sum += arr[window_end]  # add the next element
		# shrink the window as small as possible until the 'window_sum' is smaller than 's'
		while window_sum >= s:
			# more sophisticated than my if-stmt. usage
			min_length = min(min_length, window_end - window_start + 1)
			window_sum -= arr[window_start]
			window_start += 1
	if min_length == math.inf:
		return 0
	return min_length

""" Asymptotics:
For sols: (O(n+n)) = O(n) -> Sliding-Window classic, go through array once.
	from sols: "and the inner while loop processes each element only once, 
	therefore the time complexity of the algorithm will be O(N+N) 
	which is asymptotically equivalent to O(N)."
For mine: O(n) -> ?
Space complexity: O(1)
"""

# Additional code.
def main():
	print("My answer:")
	print("Smallest subarray length: " + str(MY_smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
	print("Smallest subarray length: " + str(MY_smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
	print("Smallest subarray length: " + str(MY_smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))

	print("Solutions:")
	print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
	print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
	print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))

main()
