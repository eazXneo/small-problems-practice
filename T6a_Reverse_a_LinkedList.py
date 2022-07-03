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
	current = _next
	while _next is not None:
		_next = current.next
		current.next = last
		last = current
		current = _next

	return last  # current = None (at end originally), last = new head

## ANSWER
def reverse(head):
	previous, current, next = None, head, None
	# well organised: INTERNALISE THIS!!!
	while current is not None:
		next = current.next  # temporarily store the next node
		current.next = previous  # reverse the current node
		previous = current  # before we move to the next node, point previous to the current node
		current = next  # move on the next node
	return previous

""" Asymptotics:
For sols: O(n) <- goes through list one time
For mine: O(n) <- also goes through list one time but probably doesn't run. :((
Space complexity: O(1) <- 3 pointers, irrespective of size of LL
"""


# Additional code
def main():
	MY_head = Node(2)
	MY_head.next = Node(4)
	MY_head.next.next = Node(6)
	MY_head.next.next.next = Node(8)
	MY_head.next.next.next.next = Node(10)

	print("My answer:")
	print("Nodes of original LinkedList are: ", end='')
	MY_head.print_list()
	result = MY_reverse(MY_head)
	print("Nodes of reversed LinkedList are: ", end='')
	result.print_list()

	head = Node(2)
	head.next = Node(4)
	head.next.next = Node(6)
	head.next.next.next = Node(8)
	head.next.next.next.next = Node(10)

	print("Solutions:")
	print("Nodes of original LinkedList are: ", end='')
	head.print_list()
	result = reverse(head)
	print("Nodes of reversed LinkedList are: ", end='')
	result.print_list()

main()
