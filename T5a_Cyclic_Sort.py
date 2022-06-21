# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/5.%20Pattern%20Cyclic%20Sort/Cyclic%20Sort%20(easy).py
# _Topic_ @5 Pattern: Cyclic Sort
# _Q_ @5. a)
# _Difficulty_ easy

# Problem Statement
""" 
We are given an array containing ‘n’ objects. Each object, when created, 
was assigned a unique number from 1 to ‘n’ based on their creation sequence. 
This means that the object with sequence number ‘3’ was created just 
before the object with sequence number ‘4’.
Write a function to sort the objects in-place on their creation sequence 
number in O(n) and without any extra space. 
For simplicity, let’s assume we are passed an integer array containing 
only the sequence numbers, though each number is actually an object.
Example 1:
Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
Example 2:
Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]
Example 3:
Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6]
"""

# My solution:
def MY_cyclic_sort(nums):
	# keep swapping elements until in place??
	for i, elem in enumerate(nums):
		temp = elem-1
		while i != temp:
			# swap
			nums[i] = nums[temp]
			nums[temp] = temp+1
			temp = nums[i]-1
	return nums

## ANSWER
def cyclic_sort(nums):
	i = 0
	while i < len(nums):
		j = nums[i] - 1
		if nums[i] != nums[j]:
			nums[i], nums[j] = nums[j], nums[i]  # swap
		else:
			i += 1
	return nums

""" Asymptotics:
For sols: O(n) -> each elem touched once
	"Although we are not incrementing the index i when swapping the numbers, this will result in 
	more than ‘n’ iterations of the loop, but in the worst-case scenario, the while loop will 
	swap a total of ‘n-1’ numbers and once a number is at its correct index, we will move on to 
	the next number by incrementing i. So overall, our algorithm will take O(n) + O(n-1) which is 
	asymptotically equivalent to O(n)."
For mine: O(n) -> same as above but slightly more inefficient?
Space complexity: O(1) -> we are sorting in-place by swapping elements?
"""


# Additional code
def main():
	print("My answer:")
	print(MY_cyclic_sort([3, 1, 5, 4, 2]))
	print(MY_cyclic_sort([2, 6, 4, 3, 1, 5]))
	print(MY_cyclic_sort([1, 5, 6, 4, 3, 2]))

	print("Solutions:")
	print(cyclic_sort([3, 1, 5, 4, 2]))
	print(cyclic_sort([2, 6, 4, 3, 1, 5]))
	print(cyclic_sort([1, 5, 6, 4, 3, 2]))

main()
