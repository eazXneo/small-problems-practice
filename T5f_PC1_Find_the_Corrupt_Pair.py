# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/5.%20Pattern%20Cyclic%20Sort/Problem%20Challenge%201%20-%20Find%20the%20Corrupt%20Pair%20(easy).py
# _Topic_ @5 Pattern: Cyclic Sort
# _Q_ @5. f)
# _Difficulty_ easy
# Time taken until for own solution, without compiling the code: 30 min

# Problem Statement
"""
Find the Corrupt Pair (easy)
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
The array originally contained all the numbers from 1 to ‘n’, but due to a data error, 
one of the numbers got duplicated which also resulted in one number going missing. 
Find both these numbers.
Example 1:
Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.
Example 2:
Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
"""

# My solution:
def find_corrupt_numbers(nums):
	result = [0,0]
	n = len(nums)
	# find missing num normally
	for i in range(n):
		while nums[i] != i
			if nums[i]==n:
				break
			if num[num[i]]==nums[i]:  # found dupliucate
				result[0] = nums[i]
				break
			temp = num[num[i]]
			num[num[i]] = nums[i]
			num[i] = temp
	# checking for loop doing two things.
	# find duplicate by trying to swap two of the same values.
	for w in range(n):
		if nums[i]!=i and nums[i]!=n:
			result[1] = i
	return result  # return list of two ints.
