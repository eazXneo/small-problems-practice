# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/6.%20Pattern%20In-place%20Reversal%20of%20a%20LinkedList/Reverse%20a%20LinkedList%20(easy).py
# _Topic_ @6 Pattern: In-place Reversal of a LinkedList
# _Q_ @6. a)
# _Difficulty_ easy

# Problem Statement
""" 
Given the head of a Singly LinkedList, reverse the LinkedList.
Write a function to return the new head of the reversed LinkedList.
"""

# from answer
from __future__ import print_function
# My solution:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
	# from answers:
	def print_list(self):
		temp = self
		while temp is not None:
			print(temp.value, end=" ")
			temp = temp.next
		print()

def MY_reverse(head):
	# pointer to last, curr and next
	last = head
	_next = head.next
	last.next = None
	head = _next
	while _next is not None:
		head.next = last

		last = head
		head = _next
		_next = head.next

	return head

## ANSWER
def reverse(head):
	previous, current, next = None, head, None
	while current is not None:
		next = current.next  # temporarily store the next node
		current.next = previous  # reverse the current node
		previous = current  # before we move to the next node, point previous to the current node
		current = next  # move on the next node
	return previous
