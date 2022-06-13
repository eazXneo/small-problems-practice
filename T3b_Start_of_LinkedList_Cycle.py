# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/3.%20Pattern%20Fast%20%26%20Slow%20pointers/Start%20of%20LinkedList%20Cycle%20(medium).py
# _Topic_ @3 Pattern: Fast & Slow pointers
# _Q_ @3. b)
# _Difficulty_ medium

# Problem statement:
"""
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
"""

# My solution:
# looks hard :(
class Node:
	def __init__(self, value, next=None):
		self.val = value
		self.next = next

def find_cycle_start(head):
	# use previous solution
	# then take only slow and new pointer
	# check where they meet, new pointer counts; 
	# that's the position.
	slow = head
	fast = head
	while slow.next is not None and fast.next.next is not None:
		slow = slow.next
		fast = fast.next.next
		if fast == slow:
			# found a cycle
			find_cycle = head  # new pointer
			position = 0  # counter for posision of cycle start
			while find_cycle != slow:
				find_cycle = find_cycle.next
				slow = slow.next
				position += 1
			return position
	return -1  # no cycle found
