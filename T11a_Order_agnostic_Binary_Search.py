# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/11.%20Pattern%20Modified%20Binary%20Search/Order-agnostic%20Binary%20Search%20(easy).py
# _Topic_ @11 Pattern: Pattern Modified Binary Search
# _Q_ @11. a)
# _Difficulty_ easy
# Time taken until for own solution, without compiling the code: 20 min

# Problem Statement
"""
Given a sorted array of numbers, find if a given number ‘key’ is present in the array. 
Though we know that the array is sorted, we don’t know if it’s sorted in ascending 
or descending order. You should assume that the array can have duplicates.
Write a function to return the index of the ‘key’ if it is present in the array, 
otherwise return -1.
Example 1:
Input: [4, 6, 10], key = 10
Output: 2
Example 2:
Input: [1, 2, 3, 4, 5, 6, 7], key = 5
Output: 4
Example 3:
Input: [10, 6, 4], key = 10
Output: 0
Example 4:
Input: [10, 6, 4], key = 4
Output: 2
"""

# My solution:
def binary_search(arr, key):
	index = -1
	# it's sorted, compare last and first element to determine direction
	ascending = arr[0]<arr[-1]
	if ascending:
		lower, higher = 0, len(arr)+1
		# binary search continued?
		while lower+1<higher:
			mid = (higher+lower) // 2
			if arr[mid] == key:
				index = mid
				break
			if arr[mid] > key:
				higher = mid
			else:		
				lower = mid
	else:
		lower, higher = len(arr)+1, 0
		while lower>higher+1:
			mid = (higher+lower) // 2
			if arr[mid] == key:
				index = mid
				break
			if arr[mid] > key:
				higher = mid
			else:		
				lower = mid
	return index
