# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/9.%20Pattern%20Two%20Heaps/Find%20the%20Median%20of%20a%20Number%20Stream%20(medium).py
# _Topic_ @9 Pattern: Pattern Two Heaps
# _Q_ @9. a)
# _Difficulty_ medium
# Time taken until for own solution, without compiling the code: 30 min

# Problem Statement
"""
Design a class to calculate the median of a number stream. The class should have the following two methods:
insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
Example 1:
1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5
"""

# My solution
from heapq import *

class MedianOfAStream:
	# My solution (2 below)
	minHeap = []
	maxHeap = []
	
	def insert_num(self, num):
		# check to which heap it should go
		# check sizes of heaps to see if things need to be 
		# moved from one heap to another...

		if len(minHeap) == len(maxHeap) + 1:
			# next maxHeap needs extra thing.
			# it doesn't need evening out
			if num <= minHeap[0]: # access smallest element without popping.
				heappush(maxHeap, num)
			# it does
			else:
				heappush(maxHeap, heappop(minHeap))
				heappush(maxHeap, num)
		elif len(minHeap) == len(maxHeap):
			# now it has to go to minHeap.
			if num >= minHeap[0]: # access smallest element without popping.
				heappush(minHeap, num)
			# it does
			else:
				heappush(minHeap, heappop(maxHeap))
				heappush(minHeap, num)
		else:
			print("Error?")

	def find_median(self):
		# if uneven lengths:
		if len(minHeap) == len(maxHeap) + 1:
			return minHeap[0]
		# if even take average (ignore integer overflow for now...)
		elif len(minHeap) == len(maxHeap):
			return (minHeap[0]+maxHeap[0]) / 2
		else:
			print("Error? Seems invalid heap length")
